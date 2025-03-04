from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CUserManager(BaseUserManager):
	def create_user(self, email, username, first_name, last_name, password=None):
		if not email:
			raise ValueError("Users must have an email address")
		if not password:
			raise ValueError("PLEASE ENTER AN PASSWORD")
		if not username:
			raise ValueError("Users must have an username")
		if not first_name:
			raise ValueError("Users must have a first name")
		if not last_name:
			raise ValueError("Users must have a last name")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			first_name=first_name,
			last_name=last_name
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, first_name, last_name, password=None):
		user = self.create_user(
			email,
			password=password,
			username=username,
			first_name=first_name,
			last_name=last_name
		)
		user.is_admin = True
		user.save(using=self._db)
		return user

class CUserAdminManager(models.Manager):
	def get_queryset(self):
	    return super().get_queryset().filter(is_admin=True)


class CUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True, max_length=255)
	username = models.SlugField(unique=True, max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	# custom user manager
	objects = CUserManager()
	admins = CUserAdminManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username", "first_name", "last_name"]

	prof_picture = models.ImageField(upload_to="users/prof_%Y", default="users/اصغر.jpg")
	bio = models.TextField(blank=True, max_length=500)
	phone_num = models.CharField(max_length=15, unique=True)
	birthdate = models.DateField(blank=True, null=True)
	pub_email = models.EmailField(blank=True, max_length=255)
	tel_id = models.CharField(blank=True, max_length=50)
	github_id = models.CharField(blank=True, max_length=50)
	twitt_id = models.CharField(blank=True, max_length=50)
	Youtube_id = models.CharField(blank=True, max_length=50)
	@property
	def is_staff(self):
		return self.is_admin

	def __str__(self):
		return self.username
	class Meta:
		ordering = ('id',)
	def has_perm(self, perm, obj=None):
		return self.is_admin
	def has_module_perms(self, app_label):
		return self.is_admin