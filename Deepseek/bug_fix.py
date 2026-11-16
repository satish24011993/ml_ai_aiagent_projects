

# # ─────────────────────────────────────────────────────────────────────────────

# # models.py

# # ─────────────────────────────────────────────────────────────────────────────
 
# from django.db import models

# from django.contrib.auth.models import User

# from django.utils import timezone

# from decimal import Decimal

# import hashlib
 
 
# class Customer(models.Model):

#     user        = models.OneToOneField(User, on_delete=models.CASCADE)

#     company     = models.CharField(max_length=200)

#     gst_number  = models.CharField(max_length=20, blank=True)

#     created_at  = models.DateTimeField(auto_now_add=True)
 
#     def __str__(self):

#         return self.company
 
 
# class Invoice(models.Model):

#     STATUS_CHOICES = [

#         ("draft",  "Draft"),

#         ("sent",   "Sent"),

#         ("paid",   "Paid"),

#         ("void",   "Void"),

#     ]
 
#     customer    = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="invoices")

#     status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

#     due_date    = models.DateField(null=True, blank=True)

#     created_at  = models.DateTimeField(auto_now_add=True)

#     notes       = models.TextField(blank=True)
 
#     def get_total(self):

#         """Return the sum of all line item totals."""

#         total = 0

#         for item in self.line_items.all():                     

#             total += item.quantity * item.unit_price

#         return total
 
#     def get_amount_due(self):

#         total_paid = self.payments.aggregate(

#             total=models.Sum("amount")

#         )["total"] or Decimal("0.00")

#         return self.get_total() - total_paid
 
#     def is_overdue(self):

#         if self.due_date and self.status not in ("paid", "void"):

#             return self.due_date < timezone.now().date()

#         return False
 
#     def __str__(self):

#         return f"Invoice #{self.pk} — {self.customer.company}"
 
 
# class LineItem(models.Model):

#     invoice     = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="line_items")

#     description = models.CharField(max_length=255)

#     quantity    = models.PositiveIntegerField()

#     unit_price  = models.FloatField()                          
 
#     @property

#     def line_total(self):

#         return self.quantity * self.unit_price
 
#     def __str__(self):

#         return f"{self.description} x{self.quantity}"
 
 
# class Payment(models.Model):

#     invoice     = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")

#     amount      = models.DecimalField(max_digits=10, decimal_places=2)

#     reference   = models.CharField(max_length=100, blank=True)

#     paid_at     = models.DateTimeField(auto_now_add=True)
 
#     def __str__(self):

#         return f"Payment of {self.amount} for Invoice #{self.invoice_id}"
 
 
# # ─────────────────────────────────────────────────────────────────────────────

# # utils.py

# # ─────────────────────────────────────────────────────────────────────────────
 
# def generate_invoice_pdf(invoice, line_items=[]):              

#     """

#     Build a PDF for the given invoice.

#     `line_items` can be pre-fetched and passed in to avoid extra DB hits.

#     If not provided, fetch from DB.

#     """

#     if not line_items:

#         line_items = invoice.line_items.all()
 
#     rows = []

#     for item in line_items:

#         rows.append({

#             "description": item.description,

#             "qty":         item.quantity,

#             "unit_price":  item.unit_price,

#             "total":       item.line_total,

#         })
 
#     # ... PDF generation logic (omitted for brevity) ...

#     return rows
 
 
# def apply_discount(invoice, discount_percent):

#     """

#     Return the discounted total for an invoice.

#     discount_percent is a value like 10 (meaning 10%).

#     """

#     total    = invoice.get_total()

#     discount = total * discount_percent / 100

#     return total - discount
 
 
# def send_invoice_email(invoice, recipients=[]):                

#     """Send the invoice PDF to the given list of recipients."""

#     if not recipients:

#         recipients = [invoice.customer.user.email]

#     # ... email sending logic (omitted) ...

#     print(f"Sending invoice #{invoice.pk} to {recipients}")
 
 
# def hash_api_key(raw_key):

#     """Store a hashed version of the customer's API key."""

#     return hashlib.md5(raw_key.encode()).hexdigest()           
 
 
# # ─────────────────────────────────────────────────────────────────────────────

# # views.py  (function-based views)

# # ─────────────────────────────────────────────────────────────────────────────
 
# from django.http import JsonResponse

# from django.views.decorators.http import require_http_methods

# from django.views.decorators.csrf import csrf_exempt

# from django.shortcuts import get_object_or_404

# import json
 
 
# @csrf_exempt

# @require_http_methods(["POST"])

# def create_invoice(request):

#     """Create a new draft invoice for the logged-in customer's company."""

#     if not request.user.is_authenticated:

#         return JsonResponse({"error": "Authentication required"}, status=401)
 
#     try:

#         customer = request.user.customer

#     except Customer.DoesNotExist:

#         return JsonResponse({"error": "No customer profile found"}, status=404)
 
#     body = json.loads(request.body)

#     invoice = Invoice.objects.create(

#         customer=customer,

#         notes=body.get("notes", ""),

#         due_date=body.get("due_date"),

#     )

#     return JsonResponse({"id": invoice.pk, "status": invoice.status}, status=200)  
 
 
# @csrf_exempt

# @require_http_methods(["POST"])

# def add_line_item(request, invoice_id):

#     """Add a line item to a draft invoice."""

#     if not request.user.is_authenticated:

#         return JsonResponse({"error": "Authentication required"}, status=401)
 
#     invoice = get_object_or_404(Invoice, pk=invoice_id)
 
#     if invoice.status != "draft":

#         return JsonResponse({"error": "Invoice is not in draft status"}, status=400)
 
#     body       = json.loads(request.body)

#     qty        = body.get("quantity")

#     unit_price = body.get("unit_price")

#     desc       = body.get("description")
 
#     if not all([qty, unit_price, desc]):

#         return JsonResponse({"error": "quantity, unit_price, and description required"}, status=400)
 
#     LineItem.objects.create(

#         invoice=invoice,

#         description=desc,

#         quantity=qty,

#         unit_price=unit_price,

#     )

#     return JsonResponse({"message": "Line item added", "invoice_total": invoice.get_total()})
 
 
# @csrf_exempt

# @require_http_methods(["POST"])

# def record_payment(request, invoice_id):

#     """Record a payment against an invoice and auto-mark as paid if fully settled."""

#     if not request.user.is_authenticated:

#         return JsonResponse({"error": "Authentication required"}, status=401)
 
#     invoice = get_object_or_404(Invoice, pk=invoice_id, customer__user=request.user)
 
#     if invoice.status in ("void", "paid"):

#         return JsonResponse({"error": f"Cannot pay a {invoice.status} invoice"}, status=400)
 
#     body   = json.loads(request.body)

#     amount = Decimal(str(body.get("amount", 0)))
 
#     if amount <= 0:

#         return JsonResponse({"error": "Payment amount must be positive"}, status=400)
 
#     amount_due = invoice.get_amount_due()

#     if amount > amount_due:

#         return JsonResponse({"error": f"Overpayment: amount due is {amount_due}"}, status=400)
 
#     Payment.objects.create(invoice=invoice, amount=amount)
 
#     # Auto-close invoice if fully paid

#     if invoice.get_amount_due() == Decimal("0.00"):            

#         invoice.status = "paid"

#         invoice.save()
 
#     return JsonResponse({

#         "message":    "Payment recorded",

#         "amount_due": str(invoice.get_amount_due()),

#     })
 
 
# @require_http_methods(["GET"])

# def billing_summary(request):

#     """

#     Return a billing summary for the logged-in customer.

#     {

#         "total_invoiced": ...,

#         "total_paid":     ...,

#         "total_overdue":  ...,

#         "avg_invoice":    ...

#     }

#     """

#     if not request.user.is_authenticated:

#         return JsonResponse({"error": "Authentication required"}, status=401)
 
#     invoices = Invoice.objects.filter(

#         customer__user=request.user

#     ).prefetch_related("line_items", "payments")
 
#     totals        = [inv.get_total() for inv in invoices]

#     total_invoiced = sum(totals)

#     total_paid     = sum(

#         inv.payments.aggregate(s=models.Sum("amount"))["s"] or Decimal("0.00")

#         for inv in invoices

#     )

#     overdue_invoices = [inv for inv in invoices if inv.is_overdue()]

#     total_overdue    = sum(inv.get_amount_due() for inv in overdue_invoices)
 
#     avg_invoice = total_invoiced / len(invoices)               
 
#     return JsonResponse({

#         "total_invoiced": str(total_invoiced),

#         "total_paid":     str(total_paid),

#         "total_overdue":  str(total_overdue),

#         "avg_invoice":    str(avg_invoice),

#         "invoice_count":  len(invoices),

#     })
 
 
# # ─────────────────────────────────────────────────────────────────────────────

# # signals.py

# # ─────────────────────────────────────────────────────────────────────────────
 
# from django.db.models.signals import post_save

# from django.dispatch import receiver
 
# @receiver(post_save, sender=Payment)
# def auto_close_invoice_on_full_payment(sender, instance, created, **kwargs):

#     """

#     After every payment is saved, check if the invoice is fully paid

#     and update its status automatically.

#     """
#     if not created:
#         return
#     invoice    = instance.invoice
#     amount_due = invoice.get_amount_due()
#     if amount_due <= 0:
#         invoice.status = "paid"
#         invoice.save()                                         


def reverse_str(scentence):
    return scentence[::-1]

print(reverse_str('Hello world!'))