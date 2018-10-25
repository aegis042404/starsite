from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    es = " "
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    YEAR = (
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
    )
    year = models.CharField(max_length =4, choices = YEAR)
    MONTH = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    month = models.CharField(max_length =9, choices = MONTH)
    CALL_CHOICES = (
        ('Call 1', 'Call 1'),
        ('Call 2', 'Call 2'),
        ('Call 3', 'Call 3'),
        ('Call 4', 'Call 4'),
        ('Call 5', 'Call 5'),
        ('Call 6', 'Call 6'),
        ('Call 7', 'Call 7'),
        ('Group', 'Group'),
    )
    call_choices = models.CharField(max_length = 7, choices= CALL_CHOICES)
    HOTEL_NAME = (
        ('Baudette AmericInn', 'Baudette AmericInn'),
        ('Bemidji AmericInn', 'Bemidji AmericInn'),
        ('Bismarck AmericInn', 'Bismarck AmericInn'),
        ('Fargo Country Inn & Suites', 'Fargo Country Inn & Suites'),
        ('Fargo Inn & Suites', 'Fargo Inn & Suites'),
        ('Fargo South 45 AmericInn', 'Fargo South 45 AmericInn'),
        ('Fargo West Acres AmericInn', 'Fargo West Acres AmericInn'),
        ('Fergus Falls AmericInn', 'Fergus Falls AmericInn'),
        ('Mandan Comfort Inn & Suites', 'Mandan Comfort Inn & Suites'),
        ('Minot Country Inn & Suites', 'Minot Country Inn & Suites'),
        ('Paynesville Inn & Suites', 'Paynesville Inn & Suites'),
        ('Rochester Guesthouse Inn & Suites', 'Rochester Guesthouse Inn & Suites'),
        ('Sauk Centre AmericInn', 'Sauk Centre AmericInn'),
        ('St. Cloud AmericInn', 'St. Cloud AmericInn'),
        ('Sun Valley AmericInn', 'Sun Valley AmericInn'),
        ('Valley City AmericInn', 'Valley City AmericInn'),
        ('Valley City GrandStay', 'Valley City GrandStay'),
        ('Wyndham Garden Sebastian St. Augustine', 'Wyndham Garden Sebastian St. Augustine'),
    )
    hotel_name = models.CharField(max_length = 40, choices = HOTEL_NAME)

    docfile = models.FileField(upload_to='media/%Y/%m')
    operator = models.CharField(max_length=30)
    agent = models.CharField(max_length=30)

    CA4R = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    ca4r = models.CharField(verbose_name ='Was the call answered before the 4th ring ?', max_length =3, choices = CA4R)

    AGU = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    agu = models.CharField(verbose_name = 'Was an appropriate greeting used ?',max_length = 3, choices = AGU)

    if agu == 'Yes':
        score_open += 5
    APH = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    aph = models.CharField(verbose_name = 'If you were placed on hold, did the agent ask for permission and wait for your reply?', max_length = 3, choices = APH)
    if aph == 'Yes':
        score_open += 5
    TYH = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    tyh = models.CharField(verbose_name = 'If you were placed on hold, did the agent thank you for holding when returning to the call?', max_length = 3, choices = TYH)
    if tyh == 'Yes':
        score_open += 5
    H90 = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    h90 = models.CharField(verbose_name = 'If you were placed on hold, were you on hold for more than 90 seconds? (Any call on hold for over 90 seconds will automatically be given a zero)', max_length = 3, choices = H90)

    NNCB = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    nncb = models.CharField(verbose_name = 'Did the agent ask for your name and number and offer to call you back? (2 call attempt)', max_length = 3, choices = NNCB)
    CB30 = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    cb30 = models.CharField(verbose_name = 'If yes, did an agent call you back within 30 minutes? (If yes, the call will be given a 100%.  If no, the call will be given a zero.)', max_length = 3, choices = CB30)
    AVDDA = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    avdda = models.CharField(verbose_name = 'Did the agent ask or verify dates of arrival and departure including days of the week?', max_length = 3, choices = AVDDA)

    ASB = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    asb = models.CharField(verbose_name = 'Did the agent determine if the guest has stayed at the hotel before ?', max_length = 3, choices = ASB)
    WBY = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    wby = models.CharField(verbose_name = 'Did the agent ask "what brings you to the area ?', max_length = 3, choices = WBY)
    HMPB = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    hmpb = models.CharField(verbose_name = 'Did the agent determine how many people will be traveling or how many rooms or beds would be needed ?', max_length = 3, choices = HMPB)
    UIM = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    uim = models.CharField(verbose_name = 'Did the agent describe items that make them unique in the marketplace before quoting a rate ? (N.I.C.E.)', max_length = 3, choices = UIM)
    DAQR = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    daqr = models.CharField(verbose_name = 'Did the agent describe the classic amenities before quoting a rate ?', max_length = 3, choices = DAQR)
    QR = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    qr = models.CharField(verbose_name = 'Did the agent quote a rate or rates ?', max_length = 3, choices = QR)
    US = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    us = models.CharField(verbose_name = 'Did the agent attempt to upsell by offering multiple room types or packages or clearly state that only one room type was available ?', max_length = 3, choices = US)
    SQR5 = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    sqr5 = models.CharField(verbose_name = 'Did the agent ask to make the reservation immediately after quoting the rate or rates ? (Within 5 seconds of quoting last rate.)', max_length = 3, choices = SQR5)
    UA = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    ua = models.CharField(verbose_name = 'Did you feel like you had the agents undivided attention ?', max_length = 3, choices = UA)
    TA = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    ta = models.CharField(verbose_name = 'Did the agents tone and attitude indicate a strong desire for your business ?', max_length = 3, choices = TA)
    UN = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    )
    un = models.CharField(verbose_name = 'Did the agent obtain and use the callers name in conversation at least once before asking for the reservation ?', max_length = 3, choices = UN)
    REVIEWED = (
        ('True', 'True'),
        ('False', 'False'),
    )
    reviewed = models.CharField(verbose_name = 'Make this "False"', max_length = 5, choices = REVIEWED, default = 'False')

   # variable.get_call_number_display() # should display "Call 6" or whatever it is. 
#title = str(hotel_name) + es + str(call_number)
    comments_and_suggestions = models.TextField()
################################   SCORES


########################

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.call_choices
