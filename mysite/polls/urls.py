# polls/urls.py
from django.urls import path
from . import questions
from . import choice

#添加这行 命名空间
app_name = 'polls'

# 通用视图 generic view
# 我们在这里使用两个通用视图： ListView 和 DetailView 。
# 这两个视图分别抽象“显示一个对象列表”和“显示一个特定类型对象的详细信息页面”这两种概念。使用通用视图可以大幅简化代码数量

# 通用视图修改后的代码
urlpatterns = [
    path('question/', questions.QuestionView.as_view(), name='question'),
    path('detail/<int:pk>', questions.DetailView.as_view(), name='detail'),
    path('results/<int:pk>', questions.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', questions.vote, name='vote'),
    path('addQuestion/', questions.addQuestion, name='addQuestion'),
    path('choice/', questions.choice, name='choice'),
    path('replyQuestion/<int:question_id>', questions.replyQuestion, name='replyQuestion'),
    path('delQuestion/<int:question_id>', questions.delQuestion, name='delQuestion'),
]

# 通用视图修改前的代码
# urlpatterns = [
#     path('question/', questions.question, name='question'),
#     path('detail/<int:question_id>', questions.detail, name='detail'),
#     path('results/<int:question_id>', questions.results, name='results'),
#     path('<int:question_id>/vote/', questions.vote, name='vote'),
#     path('addQuestion/', questions.addQuestion, name='addQuestion'),
#     path('choice/', questions.choice, name='choice'),
#     path('replyQuestion/<int:question_id>', questions.replyQuestion, name='replyQuestion'),
#     # path('updateBook/<int:book_id>', views1.updateBook, name='updateBook'),
#     path('delQuestion/<int:question_id>', questions.delQuestion, name='delQuestion'),
# ]