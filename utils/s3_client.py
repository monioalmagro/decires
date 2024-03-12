# Standard Libraries
import logging
from typing import Any, Union

# Third-party Libraries
from boto3.session import Session
from botocore.exceptions import ClientError

# Own Libraries
from config.enviroment_vars import settings

logger = logging.getLogger(__name__)


class AWSSessionClient:
    def __init__(self):
        self.session = self.get_session()

    @staticmethod
    async def get_session() -> Session:
        """Return Boto3 Session instance"""
        aws_settings = settings.AWS_SETTINGS
        region_name = aws_settings.AWS_REGION_NAME
        access_key = aws_settings.AWS_ACCESS_KEY_ID
        secret_key = aws_settings.AWS_SECRET_ACCESS_KEY

        if all([region_name, access_key, secret_key]):
            return Session(
                region_name=region_name,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
            )
        raise AssertionError("AWS CREDENTIALS NOT DEFINED")


class AWSS3Client(AWSSessionClient):

    __service_name: str = "s3"

    def __init__(self, bucket_name: str):
        super().__init__()
        self.bucket_name = bucket_name

    async def get_service_name(self) -> str:
        """
        Returns the name of the AWS service.

        Returns:
        ----------
        str:
            The name of the AWS service.
        """
        return self.__service_name

    async def get_client(self):
        """
        Returns a Boto3 client for the AWS service.
        """
        _service_name = await self.get_service_name()
        return await self.session.client(_service_name)

    async def put_object(
        self,
        object_key: str,
        data: Union[
            bytes,
            bytearray,
            memoryview,
        ],
    ) -> dict[str, Any]:
        """
        Uploads an object to the specified S3 bucket.

        Args:
        ----------
        object_key: str
        The key of the object to put.
        data: Union[bytes, bytearray, memoryview]
            The data to put into the object.

        Returns:
        ----------
        dict[str, Any]:
            Information about the object stored in S3. Example:
            {
                'ResponseMetadata': {
                    'RequestId': '...',
                    'HostId': '...',
                    'HTTPStatusCode': 200,
                    'HTTPHeaders': {
                        'date': '...',
                        'x-amz-request-id': '...',
                        'x-amz-id-2': '...',
                        'etag': '...'
                    },
                    'RetryAttempts': 0
                },
                'ETag': '...'
            }

        Raises:
        ----------
        Exception:
            If an error occurs while putting the object.
        """
        try:
            _client = await self.get_client()
            return _client.put_object(
                Bucket=self.bucket_name,
                Key=object_key,
                Body=data,
            )
        except ClientError as exp:
            error = repr(exp)
            logger.warning(
                (
                    f"*** AWSS3Client.put_object Failed to put object "
                    f"{object_key} to S3 bucket {self.bucket_name}: {error=}"
                ),
                exc_info=True,
            )
            raise Exception(str(exp)) from exp
        except Exception as exp:
            error = repr(exp)
            logger.error(
                f"*** AWSS3Client.put_object INTERNAL ERROR {error=} ***",
                exc_info=True,
            )
            raise Exception(str(exp)) from exp

    async def get_signed_url(
        self,
        object_key: str,
        expiration: int = 3600,  # Expiration time in seconds (default: 1 hour)
    ) -> str:
        """
        Generates a pre-signed URL for accessing the object in S3.

        Args:
        ----------
        object_key: str
            The key of the object in S3.
        expiration: int
            The expiration time for the URL in seconds (default: 3600 seconds).

        Returns:
        ----------
        str:
            The pre-signed URL for accessing the object in S3.
            ex: https://your-bucket.s3.amazonaws.com/your-image.jpg?AWSAccessKeyId=YOUR_ACCESS_KEY_ID&Expires=1636751966&Signature=SIGNATURE

        """
        try:
            client = await self.get_client()
            return client.generate_presigned_url(
                "get_object",
                Params={
                    "Bucket": self.bucket_name,
                    "Key": object_key,
                },
                ExpiresIn=expiration,
            )
        except ClientError as exp:
            logger.warning(
                (
                    f"*** AWSS3Client.get_signed_url Failed to generate "
                    f"pre-signed URL for object {object_key} in bucket "
                    f"{self.bucket_name}: {exp} ***"
                ),
                exc_info=True,
            )
            raise Exception(str(exp)) from exp
        except Exception as exp:
            logger.error(
                (
                    f"*** AWSS3Client.get_signed_url An unexpected error "
                    "occurred while generating pre-signed URL for object "
                    f"{object_key} in bucket {self.bucket_name}: {exp} ***"
                ),
                exc_info=True,
            )
            raise Exception(str(exp)) from exp
