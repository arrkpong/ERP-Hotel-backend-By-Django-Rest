#bookings\models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.core.validators import MinValueValidator

class Booking(models.Model):
    guest = models.ForeignKey("guests.Guest", on_delete=models.CASCADE, verbose_name=_("ลูกค้า"), help_text=_("ลูกค้าที่ทำการจองห้องพัก"))
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, verbose_name=_("ห้องพัก"), help_text=_("ห้องพักที่ลูกค้าทำการจอง"))
    check_in = models.DateField(verbose_name=_("วันที่เช็คอิน"), help_text=_("วันที่ลูกค้าจะเข้าพัก"))
    check_out = models.DateField(verbose_name=_("วันที่เช็คเอาท์"), help_text=_("วันที่ลูกค้าจะเช็คเอาท์"))
    cancellation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)], verbose_name=_("ค่าธรรมเนียมยกเลิก"), help_text=_("ค่าธรรมเนียมที่จะถูกเรียกเก็บหากลูกค้ายกเลิกการจอง"))
    refundable = models.BooleanField(default=True, verbose_name=_("สามารถคืนเงินได้"), help_text=_("ระบุว่าการจองนี้สามารถขอคืนเงินได้หรือไม่"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("สร้างเมื่อ"), help_text=_("วันที่และเวลาที่บันทึกการจอง"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("แก้ไขเมื่อ"), help_text=_("วันที่และเวลาที่มีการแก้ไขข้อมูลล่าสุด"))
    history = HistoricalRecords()

    def __str__(self): return f"Booking {self.id} by {self.guest}"

    class Meta:
        verbose_name = _("การจอง")
        verbose_name_plural = _("การจอง")
        ordering = ["-created_at"]
        constraints = [models.CheckConstraint(check=models.Q(check_out__gt=models.F("check_in")), name="check_out_gt_check_in")]
        indexes = [models.Index(fields=["guest"]), models.Index(fields=["room"])]

class Payment(models.Model):
    PAYMENT_METHODS = [("CASH", _("เงินสด")), ("CREDIT", _("บัตรเครดิต"))]
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, verbose_name=_("การจอง"), help_text=_("การจองที่เกี่ยวข้องกับการชำระเงินนี้"))
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS, verbose_name=_("ช่องทางการชำระเงิน"), help_text=_("วิธีการชำระเงินที่ใช้ในการทำรายการ"))
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name=_("จำนวนเงินที่ชำระ"), help_text=_("จำนวนเงินที่ลูกค้าชำระ"))
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name=_("วันที่ชำระเงิน"), help_text=_("วันที่และเวลาที่ทำรายการชำระเงิน"))
    history = HistoricalRecords()

    def __str__(self): return f"Payment for Booking {self.booking.id}"

    class Meta:
        verbose_name = _("การชำระเงิน")
        verbose_name_plural = _("การชำระเงิน")
        ordering = ["-payment_date"]
        indexes = [models.Index(fields=["booking"])]
