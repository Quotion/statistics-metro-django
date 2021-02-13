# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DonateUser(models.Model):
    sid = models.ForeignKey('MaPlayers', models.DO_NOTHING, db_column='SID_id')  # Field name made lowercase.
    donate = models.IntegerField()
    date_start = models.IntegerField()
    date_end = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donate_user'


class DsRoles(models.Model):
    role_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'ds_roles'


class DsRolesDsUsersThrough(models.Model):
    rolediscord = models.ForeignKey(DsRoles, models.DO_NOTHING)
    userdiscord = models.ForeignKey('DsUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ds_roles_ds_users_through'
        unique_together = (('rolediscord', 'userdiscord'),)


class DsUsers(models.Model):
    discord_id = models.BigIntegerField(unique=True)
    rating = models.IntegerField()
    money = models.BigIntegerField()
    gold_money = models.BigIntegerField()
    chance_roulette = models.IntegerField()
    sid = models.CharField(db_column='SID', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ds_users'


class MaAnswers(models.Model):
    sid = models.CharField(db_column='SID', max_length=20)  # Field name made lowercase.
    date = models.IntegerField()
    questions = models.IntegerField()
    status = models.IntegerField()
    answers = models.TextField()
    time = models.IntegerField()
    admin = models.TextField()
    ssadmin = models.TextField()

    class Meta:
        managed = False
        db_table = 'ma_answers'


class MaBans(models.Model):
    sid = models.ForeignKey('MaPlayers', models.DO_NOTHING, db_column='SID_id')  # Field name made lowercase.
    ban = models.SmallIntegerField()
    ban_admin = models.TextField()
    ban_reason = models.TextField()
    ban_date = models.TextField()
    unban_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'ma_bans'


class MaExaminfo(models.Model):
    sid = models.CharField(db_column='SID', max_length=20)  # Field name made lowercase.
    date = models.IntegerField()
    rank = models.TextField()
    examiner = models.TextField()
    note = models.TextField()
    type = models.IntegerField()
    server = models.TextField()

    class Meta:
        managed = False
        db_table = 'ma_examinfo'


class MaPlayers(models.Model):
    sid = models.CharField(db_column='SID', unique=True, max_length=25)  # Field name made lowercase.
    group = models.TextField()
    status = models.TextField()
    nick = models.TextField()
    synch = models.SmallIntegerField()
    synchgroup = models.TextField()

    class Meta:
        managed = False
        db_table = 'ma_players'
        default_related_name = 'player'


class MaQuestions(models.Model):
    name = models.TextField()
    questions = models.TextField()
    timelimit = models.IntegerField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ma_questions'


class MaViolations(models.Model):
    sid = models.CharField(db_column='SID', max_length=20)  # Field name made lowercase.
    date = models.IntegerField()
    admin = models.TextField()
    server = models.TextField()
    violation = models.TextField()

    class Meta:
        managed = False
        db_table = 'ma_violations'


class Newyearpresents(models.Model):
    discord = models.OneToOneField(DsUsers, models.DO_NOTHING, primary_key=True)
    present = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'newyearpresents'


class OpenidOpenidnonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=255)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'openid_openidnonce'


class OpenidOpenidstore(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'openid_openidstore'


class PlayerGroupTime(models.Model):
    sid = models.ForeignKey(MaPlayers, on_delete=models.CASCADE)  # Field name made lowercase.
    user = models.IntegerField()
    driver = models.IntegerField()
    driver3class = models.IntegerField()
    driver2class = models.IntegerField()
    all_time_on_server = models.IntegerField()
    driver1class = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_group_time'
        default_related_name = 'pgt'


class Promocodes(models.Model):
    code = models.IntegerField()
    amount = models.IntegerField()
    thing = models.IntegerField()
    creating_admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promocodes'


class Rolesgmod(models.Model):
    name = models.TextField()
    group = models.TextField()

    class Meta:
        managed = False
        db_table = 'rolesgmod'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class Statistics(models.Model):
    sid = models.CharField(db_column='SID', max_length=30)  # Field name made lowercase.
    date = models.DateField()
    ema_502 = models.IntegerField()
    lvz_540 = models.IntegerField()
    lvz_540_2 = models.IntegerField()
    lvz_540_2k = models.IntegerField()
    d_702 = models.IntegerField()
    e_703 = models.IntegerField()
    ezh_707 = models.IntegerField()
    ezh3_710 = models.IntegerField()
    msk_717 = models.IntegerField()
    lvz_717 = models.IntegerField()
    lvz_717_5k = models.IntegerField()
    msk_717_5a = models.IntegerField()
    msk_717_5m = models.IntegerField()
    lvz_717_5p = models.IntegerField()
    j717 = models.IntegerField()
    tisu_718 = models.IntegerField()
    yauza_720 = models.IntegerField()
    yauza_720_a = models.IntegerField()
    ubik_722_new = models.IntegerField()
    ubik_722 = models.IntegerField()
    ubik_722_1 = models.IntegerField()
    ubik_722_3 = models.IntegerField()
    mvm_740 = models.IntegerField()
    oka_760 = models.IntegerField()
    oka_760a = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'statistics'


class Status(models.Model):
    ip = models.CharField(unique=True, max_length=24)
    name = models.TextField()
    message = models.BigIntegerField()
    collection = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'status'
