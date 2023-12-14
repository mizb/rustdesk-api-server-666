# Generated by Django 4.2.7 on 2023-12-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="RustDesDevice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rid",
                    models.CharField(blank=True, max_length=60, verbose_name="客户端ID"),
                ),
                ("cpu", models.CharField(max_length=20, verbose_name="CPU")),
                ("hostname", models.CharField(max_length=20, verbose_name="主机名")),
                ("memory", models.CharField(max_length=20, verbose_name="内存")),
                ("os", models.CharField(max_length=20, verbose_name="操作系统")),
                ("uuid", models.CharField(max_length=60, verbose_name="uuid")),
                (
                    "username",
                    models.CharField(blank=True, max_length=60, verbose_name="系统用户名"),
                ),
                ("version", models.CharField(max_length=20, verbose_name="客户端版本")),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="设备注册时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="设备更新时间"),
                ),
            ],
            options={
                "verbose_name": "设备",
                "verbose_name_plural": "设备列表",
                "ordering": ("-rid",),
            },
        ),
        migrations.CreateModel(
            name="RustDeskPeer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.CharField(max_length=16, verbose_name="用户ID")),
                ("rid", models.CharField(max_length=60, verbose_name="客户端ID")),
                ("username", models.CharField(max_length=20, verbose_name="系统用户名")),
                ("hostname", models.CharField(max_length=30, verbose_name="操作系统名")),
                ("alias", models.CharField(max_length=30, verbose_name="别名")),
                ("platform", models.CharField(max_length=30, verbose_name="平台")),
                ("tags", models.CharField(max_length=30, verbose_name="标签")),
                ("rhash", models.CharField(max_length=60, verbose_name="设备链接密码")),
            ],
            options={
                "verbose_name": "Peers",
                "verbose_name_plural": "Peers列表",
                "ordering": ("-username",),
            },
        ),
        migrations.CreateModel(
            name="RustDeskTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.CharField(max_length=16, verbose_name="所属用户ID")),
                ("tag_name", models.CharField(max_length=60, verbose_name="标签名称")),
                (
                    "tag_color",
                    models.CharField(blank=True, max_length=60, verbose_name="标签颜色"),
                ),
            ],
            options={
                "verbose_name": "Tags",
                "verbose_name_plural": "Tags列表",
                "ordering": ("-uid",),
            },
        ),
        migrations.CreateModel(
            name="RustDeskToken",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=20, verbose_name="用户名")),
                ("rid", models.CharField(max_length=16, verbose_name="RustDesk ID")),
                ("uid", models.CharField(max_length=16, verbose_name="用户ID")),
                ("uuid", models.CharField(max_length=60, verbose_name="uuid")),
                (
                    "access_token",
                    models.CharField(
                        blank=True, max_length=60, verbose_name="access_token"
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="登录时间"),
                ),
            ],
            options={
                "verbose_name": "Token",
                "verbose_name_plural": "Token列表",
                "ordering": ("-username",),
            },
        ),
        migrations.CreateModel(
            name="ShareLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.CharField(max_length=16, verbose_name="用户ID")),
                ("shash", models.CharField(max_length=60, verbose_name="链接Key")),
                ("peers", models.CharField(max_length=20, verbose_name="机器ID列表")),
                ("is_used", models.BooleanField(default=False, verbose_name="是否使用")),
                ("is_expired", models.BooleanField(default=False, verbose_name="是否过期")),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="生成时间"),
                ),
            ],
            options={
                "verbose_name": "分享链接",
                "verbose_name_plural": "链接列表",
                "ordering": ("-create_time",),
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=50, unique=True, verbose_name="用户名"),
                ),
                ("rid", models.CharField(max_length=16, verbose_name="RustDesk ID")),
                ("uuid", models.CharField(max_length=60, verbose_name="uuid")),
                (
                    "autoLogin",
                    models.BooleanField(default=True, verbose_name="autoLogin"),
                ),
                ("rtype", models.CharField(max_length=20, verbose_name="rtype")),
                ("deviceInfo", models.TextField(blank=True, verbose_name="登录信息:")),
                ("is_active", models.BooleanField(default=True, verbose_name="是否激活")),
                ("is_admin", models.BooleanField(default=False, verbose_name="是否管理员")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "用户",
                "verbose_name_plural": "用户列表",
                "permissions": (
                    ("view_task", "Can see available tasks"),
                    ("change_task_status", "Can change the status of tasks"),
                    ("close_task", "Can remove a task by setting its status as closed"),
                ),
            },
        ),
    ]
