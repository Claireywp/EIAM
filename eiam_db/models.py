# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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


class CmdbUserinfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=50, blank=True, null=True)
    model = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cmdb_userinfo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
        managed = True
        db_table = 'django_session'


class DomainMessage(models.Model):
    did = models.AutoField(db_column='DId', primary_key=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DName', max_length=50)  # Field name made lowercase.
    ecount = models.IntegerField(db_column='ECount')  # Field name made lowercase.
    pointx = models.IntegerField(db_column='PointX')  # Field name made lowercase.
    pointy = models.IntegerField(db_column='PointY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'domain_message'


class EachMessage(models.Model):
    mid = models.AutoField(db_column='MId', primary_key=True)  # Field name made lowercase.
    resid = models.IntegerField(db_column='ResId')  # Field name made lowercase.
    reqid = models.IntegerField(db_column='ReqId')  # Field name made lowercase.
    restime = models.IntegerField(db_column='ResTIme')  # Field name made lowercase.
    state = models.IntegerField()
    estimate = models.FloatField(db_column='Estimate')  # Field name made lowercase.
    tv_e = models.FloatField(db_column='tv_E')  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'each_message'


class EntityMessage(models.Model):
    eid = models.AutoField(db_column='EId', primary_key=True)  # Field name made lowercase.
    did = models.ForeignKey(DomainMessage, models.DO_NOTHING, db_column='DId')  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=50)  # Field name made lowercase.
    context = models.CharField(db_column='Context', max_length=100)  # Field name made lowercase.
    liveness = models.FloatField(db_column='Liveness')  # Field name made lowercase.
    quality = models.FloatField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.
    energy = models.FloatField(db_column='Energy', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entity_message'


class TestmodelTest(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'testmodel_test'


class Trends(models.Model):
    tid = models.AutoField(db_column='TId', primary_key=True)  # Field name made lowercase.
    resid_t = models.IntegerField(db_column='ResId_t')  # Field name made lowercase.
    reqid_t = models.IntegerField(db_column='ReqId_t')  # Field name made lowercase.
    estimate = models.FloatField(db_column='Estimate')  # Field name made lowercase.
    t1 = models.FloatField(db_column='t1')  # Field name made lowercase.
    t2 = models.FloatField(db_column='t2')  # Field name made lowercase.
    t3 = models.FloatField(db_column='t3')  # Field name made lowercase.
    t4 = models.FloatField(db_column='t4')  # Field name made lowercase.
    t5 = models.FloatField(db_column='t5')  # Field name made lowercase.
    t6 = models.FloatField(db_column='t6')  # Field name made lowercase.
    t7 = models.FloatField(db_column='t7')  # Field name made lowercase.
    t8 = models.FloatField(db_column='t8')  # Field name made lowercase.
    # trend = models.TextField()

    class Meta:
        managed = False
        db_table = 'trends'


class GValue(models.Model):
    gid = models.AutoField(primary_key=True)
    eid = models.ForeignKey(EntityMessage, models.DO_NOTHING, db_column='eid')
    txt = models.CharField(max_length=50)
    gvalue = models.FloatField()

    class Meta:
        managed = False
        db_table = 'g_value'


class TrustD(models.Model):
    tdid = models.AutoField(db_column='TDId', primary_key=True)  # Field name made lowercase.
    senddid = models.IntegerField(db_column='sendDId')  # Field name made lowercase.
    backdid = models.IntegerField(db_column='backDId')  # Field name made lowercase.
    distance = models.FloatField(db_column='Distance')  # Field name made lowercase.
    tv_d = models.FloatField()

    class Meta:
        managed = False
        db_table = 'trust_d'
