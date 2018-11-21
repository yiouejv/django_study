#encoding: utf-8

from django import forms

TOPIC_CHOICE = (
    ('5', '超级好评'),
    ('4', '好评'),
    ('3', '中评'),
    ('2', '差评'),
    ('1', '极差'),
)

# 表示评论内容的表单控件的class
# 评论标题 - 文本框
# 电子邮件 - 邮件框
# 评论内容 - Textarea
# 评论级别 - 下拉选择框
# 是否保存 - 复选框
class RemarkForm(forms.Form):  # remark 评论
    '''
        subject: forms.CharField 生成文本框， 评论主题，label表示评论前的文本标签
        email: forms.EmailField email框
        message: 评论内容
        topic: 评论级别
        is_save: 是否保存
    '''
    subject = forms.CharField(label='标题')  # 主题
    email = forms.EmailField(label='电子邮件')
    # widget=forms.Textarea 将当前的单行文本框变为多行文本域
    message = forms.CharField(label='内容', widget=forms.Textarea)
    # forms.ChoiceField()  下拉列表框
    topic = forms.ChoiceField(label='级别', choices=TOPIC_CHOICE)
    is_save = forms.BooleanField(label='是否保存')



class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.CharField()
    email = forms.EmailField()



