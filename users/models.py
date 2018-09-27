from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import choices


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30)
    perfil = models.CharField(max_length=255, choices=choices.PERFIL_CHOICES, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    celular = models.CharField(max_length=255, blank=True, null=True)
    empresa = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-creado',)
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
        permissions = (
            ('perm_ni_administrador', 'Permisos para NI Administrador'),
            ('perm_ni_visitante', 'Permisos para NI Visitante'),
            ('perm_ni_rastreo', 'Permisos para NI Rastreo'),
            ('perm_ni_proceso', 'Permisos para NI Proceso'),
        )

    def __str__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        user = self.user
        if user.is_active and self.perfil:
            perfil = self.perfil
            new_perfil, new = Perfil.objects.get_or_create(user=self.user)
            new_group, new= Group.objects.get_or_create(name=perfil)
            permission = Permission.objects.get(name='Permisos para '+ perfil)
            new_group.permissions.add(permission)
            user.groups.add(new_group)
            self.slug = slugify(self.user)
            super(Perfil, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.user)
            super(Perfil, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('users:detail_perfil', kwargs={'slug': self.slug})

    @receiver(post_save, sender=User)
    def create_perfil(sender, instance, created, **kwargs):
        if created:
            perfil, new = Perfil.objects.get_or_create(user=instance,
                                                       nombre=instance.first_name,
                                                       apellido=instance.last_name,
                                                       email=instance.email,
                                                       nombre_completo=instance.get_full_name(),
                                                       )

    @receiver(post_save, sender=User)
    def save_perfil(sender, instance, **kwargs):
        try:
            instance.perfil.save()
        except:
            pass
