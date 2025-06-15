from django.conf import settings

def project_name(request):
    """
    全てのテンプレートで {{ PROJECT_NAME }} を使えるようにする
    """
    return {
        'PROJECT_NAME': settings.PROJECT_NAME
    }
