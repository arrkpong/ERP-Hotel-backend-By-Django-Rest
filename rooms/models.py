#rooms\models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

class RoomStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", _("ว่าง")
    BOOKED = "BOOKED", _("ถูกจอง")
    MAINTENANCE = "MAINTENANCE", _("อยู่ระหว่างซ่อมแซม")

class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("ชื่อสิ่งอำนวยความสะดวก"), help_text=_("เช่น Wi-Fi, ทีวี, เครื่องปรับอากาศ"))
    description = models.TextField(null=True, blank=True, verbose_name=_("รายละเอียด"), help_text=_("คำอธิบายเพิ่มเติมเกี่ยวกับสิ่งอำนวยความสะดวก"))
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("สิ่งอำนวยความสะดวก")
        verbose_name_plural = _("สิ่งอำนวยความสะดวก")
        ordering = ["name"]

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True, verbose_name=_("หมายเลขห้อง"), help_text=_("เช่น 101, 102, 201"))
    type = models.CharField(max_length=100, verbose_name=_("ประเภทห้อง"), help_text=_("เช่น ห้องเดี่ยว, ห้องคู่, ห้องสวีท"))
    status = models.CharField(max_length=20, choices=RoomStatus.choices, default=RoomStatus.AVAILABLE, verbose_name=_("สถานะ"), help_text=_("ว่าง, ถูกจอง, อยู่ระหว่างซ่อมแซม"))
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("ราคาต่อคืน"), help_text=_("ราคาห้องพักต่อคืน"))
    size = models.FloatField(verbose_name=_("พื้นที่ห้อง (ตารางเมตร)"), help_text=_("พื้นที่ของห้องพักในหน่วยตารางเมตร"))
    amenities = models.ManyToManyField(Amenity, through="RoomAmenity", verbose_name=_("สิ่งอำนวยความสะดวก"), help_text=_("สิ่งอำนวยความสะดวกในห้อง"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("สร้างเมื่อ"), help_text=_("วันที่และเวลาที่ห้องพักถูกเพิ่มเข้าระบบ"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("แก้ไขเมื่อ"), help_text=_("วันที่และเวลาที่ข้อมูลห้องพักถูกแก้ไขล่าสุด"))
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.number} ({self.type})"

    class Meta:
        verbose_name = _("ห้องพัก")
        verbose_name_plural = _("ห้องพัก")
        ordering = ["number"]

class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name=_("ห้องพัก"), help_text=_("ห้องพักที่มีสิ่งอำนวยความสะดวกนี้"))
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE, verbose_name=_("สิ่งอำนวยความสะดวก"), help_text=_("สิ่งอำนวยความสะดวกที่เชื่อมต่อกับห้องพัก"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("จำนวน"), help_text=_("จำนวนของสิ่งอำนวยความสะดวก เช่น จำนวนเครื่องปรับอากาศ"))
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.room} - {self.amenity} ({self.quantity})"

    class Meta:
        verbose_name = _("สิ่งอำนวยความสะดวกในห้องพัก")
        verbose_name_plural = _("สิ่งอำนวยความสะดวกในห้องพัก")
