# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Albums(models.Model):
    albumid = models.AutoField(db_column='AlbumId', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase. This field type is a guess.
    artistid = models.ForeignKey('Artists', models.DO_NOTHING, db_column='ArtistId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'albums'


class Artists(models.Model):
    artistid = models.AutoField(db_column='ArtistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'artists'


class Customers(models.Model):
    customerid = models.AutoField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='Company', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email')  # Field name made lowercase. This field type is a guess.
    supportrepid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='SupportRepId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='ReportsTo', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'employees'


class Genres(models.Model):
    genreid = models.AutoField(db_column='GenreId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'genres'


class InvoiceItems(models.Model):
    invoicelineid = models.AutoField(db_column='InvoiceLineId', primary_key=True)  # Field name made lowercase.
    invoiceid = models.ForeignKey('Invoices', models.DO_NOTHING, db_column='InvoiceId')  # Field name made lowercase.
    trackid = models.ForeignKey('Tracks', models.DO_NOTHING, db_column='TrackId')  # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice')  # Field name made lowercase. This field type is a guess.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice_items'


class Invoices(models.Model):
    invoiceid = models.AutoField(db_column='InvoiceId', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate')  # Field name made lowercase.
    billingaddress = models.TextField(db_column='BillingAddress', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    billingcity = models.TextField(db_column='BillingCity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    billingstate = models.TextField(db_column='BillingState', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    billingcountry = models.TextField(db_column='BillingCountry', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    billingpostalcode = models.TextField(db_column='BillingPostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total = models.TextField(db_column='Total')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'invoices'


class MediaTypes(models.Model):
    mediatypeid = models.AutoField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'media_types'


class PlaylistTrack(models.Model):
    playlistid = models.OneToOneField('Playlists', models.DO_NOTHING, db_column='PlaylistId', primary_key=True)  # Field name made lowercase. The composite primary key (PlaylistId, TrackId) found, that is not supported. The first column is selected.
    trackid = models.ForeignKey('Tracks', models.DO_NOTHING, db_column='TrackId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playlist_track'


class Playlists(models.Model):
    playlistid = models.AutoField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'playlists'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Tracks(models.Model):
    trackid = models.AutoField(db_column='TrackId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    albumid = models.ForeignKey(Albums, models.DO_NOTHING, db_column='AlbumId', blank=True, null=True)  # Field name made lowercase.
    mediatypeid = models.ForeignKey(MediaTypes, models.DO_NOTHING, db_column='MediaTypeId')  # Field name made lowercase.
    genreid = models.ForeignKey(Genres, models.DO_NOTHING, db_column='GenreId', blank=True, null=True)  # Field name made lowercase.
    composer = models.TextField(db_column='Composer', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    milliseconds = models.IntegerField(db_column='Milliseconds')  # Field name made lowercase.
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tracks'
