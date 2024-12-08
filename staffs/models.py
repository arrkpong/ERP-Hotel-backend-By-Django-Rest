from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from simple_history.models import HistoricalRecords

class PositionChoices(models.TextChoices):
    MANAGER = 'Manager', _("ผู้จัดการ")
    STAFF = 'Staff', _("เจ้าหน้าที่")
    DEVELOPER = 'Developer', _("นักพัฒนา")
    INTERN = 'Intern', _("นักศึกษาฝึกงาน")

class Staff(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_("ชื่อเต็ม"),help_text=_("กรุณากรอกชื่อเต็มของพนักงาน"))
    email = models.EmailField(unique=True, verbose_name=_("อีเมล"),help_text=_("กรุณากรอกอีเมลที่สามารถติดต่อได้"))
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{9,15}$', _("กรุณากรอกหมายเลขโทรศัพท์ที่ถูกต้อง (9-15 ตัวเลข)"))],verbose_name=_("เบอร์โทรศัพท์"),help_text=_("กรุณากรอกหมายเลขโทรศัพท์ที่สามารถติดต่อได้ (9-15 ตัวเลข)"))
    position = models.CharField(max_length=50, choices=PositionChoices.choices, default=PositionChoices.STAFF, verbose_name=_("ตำแหน่ง"),help_text=_("เลือกตำแหน่งของพนักงาน"))
    hire_date = models.DateField(verbose_name=_("วันที่เข้าทำงาน"),help_text=_("กรุณาเลือกวันที่เข้าทำงานของพนักงาน"))
    is_active = models.BooleanField(default=True, verbose_name=_("สถานะการใช้งาน"), help_text=_("กำหนดว่าพนักงานยังคงทำงานอยู่หรือไม่"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("สร้างเมื่อ"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("แก้ไขเมื่อ"))
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.full_name} ({self.position})"

    class Meta:
        verbose_name = _("พนักงาน")
        verbose_name_plural = _("พนักงาน")
        ordering = ["full_name"]
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["phone"])
        ]
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_email"),
            models.UniqueConstraint(fields=["phone"], name="unique_phone")
        ]
