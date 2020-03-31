from django.forms import ModelForm
from.models import PostModel, CommentModel


class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ['title','content','header_image','category']

class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['commented_by','content']
