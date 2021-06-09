from graphene import relay, ObjectType, Mutation, Boolean, ID
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_file_upload.scalars import Upload
import boto3
import uuid

from .models import Author, Book, BookImage
from .filters import BookFilter
from .api.serializers import AuthorSerializer, BookSerializer

# AWS S3 Bucket
S3_BASE_URL = 's3.amazonaws.com'
BUCKET = 'django_library_project'


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        interfaces = (relay.Node, )


class BookImageNode(DjangoObjectType):
    class Meta:
        model = BookImage


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = []
        interfaces = (relay.Node, )


class BookMutation(SerializerMutation):
    class Meta:
        serializer_class = BookSerializer


class BookImageMutation(Mutation):
    success = Boolean()

    class Arguments:
        file = Upload(required=True)
        id = ID(required=True)

    def mutate(self, info, file, **data):
        photo_file = file
        book_id = data.get('id')
        if photo_file and book_id:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(photo_file, BUCKET, key)
                url = f'https://{BUCKET}.{S3_BASE_URL}/{key}'
                photo = BookImage(url=url, book_id=book_id)
                photo.save()
            except Exception as err:
                print('There was a problem uploading the image: %s' % err)
                return BookImageMutation(success=False)
        else:
            print('Missing book id or image file')
            return BookImageMutation(success=False)
        return BookImageMutation(success=True)


class AuthorMutation(SerializerMutation):
    class Meta:
        serializer_class = AuthorSerializer


class Query(ObjectType):
    book = relay.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode, filterset_class=BookFilter)
    author = relay.Node.Field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode)


class Mutation(ObjectType):
    book_mutation = BookMutation.Field()
    book_image_mutation = BookImageMutation.Field()
    author_mutation = AuthorMutation.Field()
