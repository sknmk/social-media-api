## Social Media API

---
### Python - Django - DRF 

---
- Users
- User Profiles
- Posts
- Post Reactions
- Comments
- Comment Reactions
---

- Browsable API
- Basic Auth
- Token Auth
- Super User Permissions
- IsOwnerOrReadOnly Permissions
- Unit Tests (98% Coverage)
- ---

#### URL Table
|/                                                        |rest_framework.routers.APIRootView                  |api-root                             |
|---------------------------------------------------------|----------------------------------------------------|-------------------------------------|
|/\.<format>/                                             |rest_framework.routers.APIRootView                  |api-root                             |
|/__debug__/history_refresh/                              |debug_toolbar.panels.history.views.history_refresh  |djdt:history_refresh                 |
|/__debug__/history_sidebar/                              |debug_toolbar.panels.history.views.history_sidebar  |djdt:history_sidebar                 |
|/__debug__/render_panel/                                 |debug_toolbar.views.render_panel                    |djdt:render_panel                    |
|/__debug__/sql_explain/                                  |debug_toolbar.panels.sql.views.sql_explain          |djdt:sql_explain                     |
|/__debug__/sql_profile/                                  |debug_toolbar.panels.sql.views.sql_profile          |djdt:sql_profile                     |
|/__debug__/sql_select/                                   |debug_toolbar.panels.sql.views.sql_select           |djdt:sql_select                      |
|/__debug__/template_source/                              |debug_toolbar.panels.templates.views.template_source|djdt:template_source                 |
|/admin/                                                  |django.contrib.admin.sites.index                    |admin:index                          |
|/admin/<app_label>/                                      |django.contrib.admin.sites.app_index                |admin:app_list                       |
|/admin/<url>                                             |django.contrib.admin.sites.catch_all_view           |                                     |
|/admin/account/emailaddress/                             |django.contrib.admin.options.changelist_view        |admin:account_emailaddress_changelist|
|/admin/account/emailaddress/<path:object_id>/            |django.views.generic.base.RedirectView              |                                     |
|/admin/account/emailaddress/<path:object_id>/change/     |django.contrib.admin.options.change_view            |admin:account_emailaddress_change    |
|/admin/account/emailaddress/<path:object_id>/delete/     |django.contrib.admin.options.delete_view            |admin:account_emailaddress_delete    |
|/admin/account/emailaddress/<path:object_id>/history/    |django.contrib.admin.options.history_view           |admin:account_emailaddress_history   |
|/admin/account/emailaddress/add/                         |django.contrib.admin.options.add_view               |admin:account_emailaddress_add       |
|/admin/auth/group/                                       |django.contrib.admin.options.changelist_view        |admin:auth_group_changelist          |
|/admin/auth/group/<path:object_id>/                      |django.views.generic.base.RedirectView              |                                     |
|/admin/auth/group/<path:object_id>/change/               |django.contrib.admin.options.change_view            |admin:auth_group_change              |
|/admin/auth/group/<path:object_id>/delete/               |django.contrib.admin.options.delete_view            |admin:auth_group_delete              |
|/admin/auth/group/<path:object_id>/history/              |django.contrib.admin.options.history_view           |admin:auth_group_history             |
|/admin/auth/group/add/                                   |django.contrib.admin.options.add_view               |admin:auth_group_add                 |
|/admin/auth/user/                                        |django.contrib.admin.options.changelist_view        |admin:auth_user_changelist           |
|/admin/auth/user/<id>/password/                          |django.contrib.auth.admin.user_change_password      |admin:auth_user_password_change      |
|/admin/auth/user/<path:object_id>/                       |django.views.generic.base.RedirectView              |                                     |
|/admin/auth/user/<path:object_id>/change/                |django.contrib.admin.options.change_view            |admin:auth_user_change               |
|/admin/auth/user/<path:object_id>/delete/                |django.contrib.admin.options.delete_view            |admin:auth_user_delete               |
|/admin/auth/user/<path:object_id>/history/               |django.contrib.admin.options.history_view           |admin:auth_user_history              |
|/admin/auth/user/add/                                    |django.contrib.auth.admin.add_view                  |admin:auth_user_add                  |
|/admin/authtoken/tokenproxy/                             |django.contrib.admin.options.changelist_view        |admin:authtoken_tokenproxy_changelist|
|/admin/authtoken/tokenproxy/<path:object_id>/            |django.views.generic.base.RedirectView              |                                     |
|/admin/authtoken/tokenproxy/<path:object_id>/change/     |django.contrib.admin.options.change_view            |admin:authtoken_tokenproxy_change    |
|/admin/authtoken/tokenproxy/<path:object_id>/delete/     |django.contrib.admin.options.delete_view            |admin:authtoken_tokenproxy_delete    |
|/admin/authtoken/tokenproxy/<path:object_id>/history/    |django.contrib.admin.options.history_view           |admin:authtoken_tokenproxy_history   |
|/admin/authtoken/tokenproxy/add/                         |django.contrib.admin.options.add_view               |admin:authtoken_tokenproxy_add       |
|/admin/autocomplete/                                     |django.contrib.admin.sites.autocomplete_view        |admin:autocomplete                   |
|/admin/comments/comment/                                 |django.contrib.admin.options.changelist_view        |admin:comments_comment_changelist    |
|/admin/comments/comment/<path:object_id>/                |django.views.generic.base.RedirectView              |                                     |
|/admin/comments/comment/<path:object_id>/change/         |django.contrib.admin.options.change_view            |admin:comments_comment_change        |
|/admin/comments/comment/<path:object_id>/delete/         |django.contrib.admin.options.delete_view            |admin:comments_comment_delete        |
|/admin/comments/comment/<path:object_id>/history/        |django.contrib.admin.options.history_view           |admin:comments_comment_history       |
|/admin/comments/comment/add/                             |django.contrib.admin.options.add_view               |admin:comments_comment_add           |
|/admin/jsi18n/                                           |django.contrib.admin.sites.i18n_javascript          |admin:jsi18n                         |
|/admin/login/                                            |django.contrib.admin.sites.login                    |admin:login                          |
|/admin/logout/                                           |django.contrib.admin.sites.logout                   |admin:logout                         |
|/admin/password_change/                                  |django.contrib.admin.sites.password_change          |admin:password_change                |
|/admin/password_change/done/                             |django.contrib.admin.sites.password_change_done     |admin:password_change_done           |
|/admin/posts/post/                                       |django.contrib.admin.options.changelist_view        |admin:posts_post_changelist          |
|/admin/posts/post/<path:object_id>/                      |django.views.generic.base.RedirectView              |                                     |
|/admin/posts/post/<path:object_id>/change/               |django.contrib.admin.options.change_view            |admin:posts_post_change              |
|/admin/posts/post/<path:object_id>/delete/               |django.contrib.admin.options.delete_view            |admin:posts_post_delete              |
|/admin/posts/post/<path:object_id>/history/              |django.contrib.admin.options.history_view           |admin:posts_post_history             |
|/admin/posts/post/add/                                   |django.contrib.admin.options.add_view               |admin:posts_post_add                 |
|/admin/r/<int:content_type_id>/<path:object_id>/         |django.contrib.contenttypes.views.shortcut          |admin:view_on_site                   |
|/admin/sites/site/                                       |django.contrib.admin.options.changelist_view        |admin:sites_site_changelist          |
|/admin/sites/site/<path:object_id>/                      |django.views.generic.base.RedirectView              |                                     |
|/admin/sites/site/<path:object_id>/change/               |django.contrib.admin.options.change_view            |admin:sites_site_change              |
|/admin/sites/site/<path:object_id>/delete/               |django.contrib.admin.options.delete_view            |admin:sites_site_delete              |
|/admin/sites/site/<path:object_id>/history/              |django.contrib.admin.options.history_view           |admin:sites_site_history             |
|/admin/sites/site/add/                                   |django.contrib.admin.options.add_view               |admin:sites_site_add                 |
|/admin/users/userprofile/                                |django.contrib.admin.options.changelist_view        |admin:users_userprofile_changelist   |
|/admin/users/userprofile/<path:object_id>/               |django.views.generic.base.RedirectView              |                                     |
|/admin/users/userprofile/<path:object_id>/change/        |django.contrib.admin.options.change_view            |admin:users_userprofile_change       |
|/admin/users/userprofile/<path:object_id>/delete/        |django.contrib.admin.options.delete_view            |admin:users_userprofile_delete       |
|/admin/users/userprofile/<path:object_id>/history/       |django.contrib.admin.options.history_view           |admin:users_userprofile_history      |
|/admin/users/userprofile/add/                            |django.contrib.admin.options.add_view               |admin:users_userprofile_add          |
|/api/basic-auth/login/                                   |django.contrib.auth.views.LoginView                 |rest_framework:login                 |
|/api/basic-auth/logout/                                  |django.contrib.auth.views.LogoutView                |rest_framework:logout                |
|/api/token-auth/login/                                   |rest_auth.views.LoginView                           |rest_login                           |
|/api/token-auth/logout/                                  |rest_auth.views.LogoutView                          |rest_logout                          |
|/api/token-auth/password/change/                         |rest_auth.views.PasswordChangeView                  |rest_password_change                 |
|/api/token-auth/password/reset/                          |rest_auth.views.PasswordResetView                   |rest_password_reset                  |
|/api/token-auth/password/reset/confirm/                  |rest_auth.views.PasswordResetConfirmView            |rest_password_reset_confirm          |
|/api/token-auth/registration/                            |rest_auth.registration.views.RegisterView           |rest_register                        |
|/api/token-auth/registration/account-confirm-email/<key>/|django.views.generic.base.TemplateView              |account_confirm_email                |
|/api/token-auth/registration/verify-email/               |rest_auth.registration.views.VerifyEmailView        |rest_verify_email                    |
|/api/token-auth/user/                                    |rest_auth.views.UserDetailsView                     |rest_user_details                    |
|/posts/                                                  |timeline.posts.views.PostViewSet                    |post-list                            |
|/posts/<pk>/                                             |timeline.posts.views.PostViewSet                    |post-detail                          |
|/posts/<pk>\.<format>/                                   |timeline.posts.views.PostViewSet                    |post-detail                          |
|/posts/<post_pk>/comments/                               |timeline.comments.views.CommentViewSet              |comment-list                         |
|/posts/<post_pk>/comments/<comment_pk>/reactions/        |timeline.reactions.views.UserCommentReactionsViewSet|comment-reactions-list               |
|/posts/<post_pk>/comments/<comment_pk>/reactions/<pk>/   |timeline.reactions.views.UserCommentReactionsViewSet|comment-reactions-detail             |
|/posts/<post_pk>/comments/<pk>/                          |timeline.comments.views.CommentViewSet              |comment-detail                       |
|/posts/<post_pk>/reactions/                              |timeline.reactions.views.UserPostReactionsViewSet   |post-reactions-list                  |
|/posts/<post_pk>/reactions/<pk>/                         |timeline.reactions.views.UserPostReactionsViewSet   |post-reactions-detail                |
|/posts\.<format>/                                        |timeline.posts.views.PostViewSet                    |post-list                            |
|/user/profile/<user_id>/                                 |timeline.users.views.UserProfileViewSet             |user-profile-detail                  |
|/user/profile/<user_id>\.<format>/                       |timeline.users.views.UserProfileViewSet             |user-profile-detail                  |
|/users/                                                  |timeline.users.views.UserViewSet                    |user-list                            |
|/users/<pk>/                                             |timeline.users.views.UserViewSet                    |user-detail                          |
|/users/<pk>\.<format>/                                   |timeline.users.views.UserViewSet                    |user-detail                          |
|/users\.<format>/                                        |timeline.users.views.UserViewSet                    |user-list                            |
