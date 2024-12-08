#guests\models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

class Guest(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_("ชื่อเต็ม"), help_text=_("ชื่อเต็มของลูกค้า"))
    email = models.EmailField(unique=True, verbose_name=_("อีเมล"), help_text=_("อีเมลที่ใช้ในการติดต่อหรือทำการจอง"))
    phone = models.CharField(max_length=15, verbose_name=_("เบอร์โทรศัพท์"), help_text=_("หมายเลขโทรศัพท์ของลูกค้า"))
    id_card_number = models.CharField(max_length=13, unique=True, null=True, blank=True, verbose_name=_("เลขบัตรประชาชน"), help_text=_("หมายเลขบัตรประชาชนของลูกค้า"))
    address = models.TextField(null=True, blank=True, verbose_name=_("ที่อยู่"), help_text=_("ที่อยู่ของลูกค้า (อาจจะเป็นที่อยู่สำหรับการจัดส่งเอกสารหรือการเช็คอิน)"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("สร้างเมื่อ"), help_text=_("วันที่และเวลาที่ลูกค้าถูกบันทึกเข้าระบบ"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("แก้ไขเมื่อ"), help_text=_("วันที่และเวลาที่ข้อมูลของลูกค้าถูกแก้ไขล่าสุด"))
    history = HistoricalRecords()

    def __str__(self): return self.full_name

    class Meta:
        verbose_name = _("ลูกค้า")
        verbose_name_plural = _("ลูกค้า")
        ordering = ["full_name"]
        indexes = [models.Index(fields=["email"]), models.Index(fields=["phone"])]
