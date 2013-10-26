# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class ArticlesArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100L)
    slug = models.CharField(max_length=50L)
    status_id = models.IntegerField()
    author_id = models.IntegerField()
    keywords = models.TextField()
    description = models.TextField()
    markup = models.CharField(max_length=1L)
    content = models.TextField()
    rendered_content = models.TextField()
    auto_tag = models.IntegerField()
    publish_date = models.DateTimeField()
    expiration_date = models.DateTimeField(null=True, blank=True)
    is_active = models.IntegerField()
    login_required = models.IntegerField()
    use_addthis_button = models.IntegerField()
    addthis_use_author = models.IntegerField()
    addthis_username = models.CharField(max_length=50L)
    image_url = models.TextField()
    class Meta:
        db_table = 'articles_article'

class ArticlesArticleCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    category_id = models.IntegerField()
    class Meta:
        db_table = 'articles_article_categories'

class ArticlesArticleFollowupFor(models.Model):
    id = models.IntegerField(primary_key=True)
    from_article_id = models.IntegerField()
    to_article_id = models.IntegerField()
    class Meta:
        db_table = 'articles_article_followup_for'

class ArticlesArticleMerchants(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    merchant_id = models.IntegerField()
    class Meta:
        db_table = 'articles_article_merchants'

class ArticlesArticleRelatedArticles(models.Model):
    id = models.IntegerField(primary_key=True)
    from_article_id = models.IntegerField()
    to_article_id = models.IntegerField()
    class Meta:
        db_table = 'articles_article_related_articles'

class ArticlesArticleSites(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    site_id = models.IntegerField()
    class Meta:
        db_table = 'articles_article_sites'

class ArticlesArticleTags(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = 'articles_article_tags'

class ArticlesArticlestatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    ordering = models.IntegerField()
    is_live = models.IntegerField()
    class Meta:
        db_table = 'articles_articlestatus'

class ArticlesAttachment(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField()
    attachment = models.CharField(max_length=100L)
    caption = models.CharField(max_length=255L)
    class Meta:
        db_table = 'articles_attachment'

class ArticlesTag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64L, unique=True)
    slug = models.CharField(max_length=64L, unique=True, blank=True)
    class Meta:
        db_table = 'articles_tag'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = 'auth_user_user_permissions'

class BlogCommentmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'blog_commentmeta'

class BlogComments(models.Model):
    comment_id = models.BigIntegerField(primary_key=True, db_column='comment_ID') # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID') # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100L)
    comment_author_url = models.CharField(max_length=200L)
    comment_author_ip = models.CharField(max_length=100L, db_column='comment_author_IP') # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20L)
    comment_agent = models.CharField(max_length=255L)
    comment_type = models.CharField(max_length=20L)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()
    class Meta:
        db_table = 'blog_comments'

class BlogLinks(models.Model):
    link_id = models.BigIntegerField(primary_key=True)
    link_url = models.CharField(max_length=255L)
    link_name = models.CharField(max_length=255L)
    link_image = models.CharField(max_length=255L)
    link_target = models.CharField(max_length=25L)
    link_description = models.CharField(max_length=255L)
    link_visible = models.CharField(max_length=20L)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255L)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255L)
    class Meta:
        db_table = 'blog_links'

class BlogOptions(models.Model):
    option_id = models.BigIntegerField(primary_key=True)
    option_name = models.CharField(max_length=64L, unique=True)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20L)
    class Meta:
        db_table = 'blog_options'

class BlogPostmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'blog_postmeta'

class BlogPosts(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20L)
    comment_status = models.CharField(max_length=20L)
    ping_status = models.CharField(max_length=20L)
    post_password = models.CharField(max_length=20L)
    post_name = models.CharField(max_length=200L)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255L)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20L)
    post_mime_type = models.CharField(max_length=100L)
    comment_count = models.BigIntegerField()
    class Meta:
        db_table = 'blog_posts'

class BlogTermRelationships(models.Model):
    object_id = models.BigIntegerField()
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()
    class Meta:
        db_table = 'blog_term_relationships'

class BlogTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigIntegerField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32L)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()
    class Meta:
        db_table = 'blog_term_taxonomy'

class BlogTerms(models.Model):
    term_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200L)
    slug = models.CharField(max_length=200L, unique=True)
    term_group = models.BigIntegerField()
    class Meta:
        db_table = 'blog_terms'

class BlogUsermeta(models.Model):
    umeta_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255L, blank=True)
    meta_value = models.TextField(blank=True)
    class Meta:
        db_table = 'blog_usermeta'

class BlogUsers(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    user_login = models.CharField(max_length=60L)
    user_pass = models.CharField(max_length=64L)
    user_nicename = models.CharField(max_length=50L)
    user_email = models.CharField(max_length=100L)
    user_url = models.CharField(max_length=100L)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=60L)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250L)
    class Meta:
        db_table = 'blog_users'

class CoreCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    ref_id = models.CharField(max_length=255L)
    code = models.CharField(max_length=255L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    image = models.TextField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'core_category'

class CoreCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255L)
    name = models.CharField(max_length=255L)
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'core_country'

class CoreCoupon(models.Model):
    id = models.IntegerField(primary_key=True)
    ref_id = models.CharField(max_length=255L)
    merchant_id = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    restrictions = models.TextField(blank=True)
    code = models.CharField(max_length=255L, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    link = models.TextField(blank=True)
    directlink = models.TextField(blank=True)
    skimlinks = models.TextField(blank=True)
    status = models.CharField(max_length=255L, blank=True)
    lastupdated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()
    listprice = models.FloatField()
    discount = models.FloatField()
    percent = models.IntegerField()
    image = models.TextField(blank=True)
    short_desc = models.CharField(max_length=50L)
    desc_slug = models.CharField(max_length=175L)
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    embedly_title = models.TextField(blank=True)
    embedly_description = models.TextField(blank=True)
    embedly_image_url = models.TextField(blank=True)
    class Meta:
        db_table = 'core_coupon'

class CoreCouponCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    coupon_id = models.IntegerField()
    category_id = models.IntegerField()
    class Meta:
        db_table = 'core_coupon_categories'

class CoreCouponCountries(models.Model):
    id = models.IntegerField(primary_key=True)
    coupon_id = models.IntegerField()
    country_id = models.IntegerField()
    class Meta:
        db_table = 'core_coupon_countries'

class CoreCouponDealtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    coupon_id = models.IntegerField()
    dealtype_id = models.IntegerField()
    class Meta:
        db_table = 'core_coupon_dealtypes'

class CoreCouponnetwork(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'core_couponnetwork'

class CoreDealtype(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255L, blank=True)
    name = models.CharField(max_length=255L, blank=True)
    description = models.CharField(max_length=255L, blank=True)
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'core_dealtype'

class CoreMerchant(models.Model):
    id = models.IntegerField(primary_key=True)
    ref_id = models.CharField(max_length=255L)
    name = models.CharField(max_length=255L)
    name_slug = models.CharField(max_length=255L)
    image = models.TextField()
    description = models.TextField()
    link = models.TextField(blank=True)
    directlink = models.TextField(blank=True)
    skimlinks = models.TextField(blank=True)
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    coupon_count = models.IntegerField()
    redirect = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'core_merchant'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255L)
    migration = models.CharField(max_length=255L)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'south_migrationhistory'

class TrackingAcquisitionsource(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=255L, unique=True)
    logo_url = models.CharField(max_length=255L)
    class Meta:
        db_table = 'tracking_acquisitionsource'

class TrackingBannedip(models.Model):
    id = models.IntegerField(primary_key=True)
    ip_address = models.CharField(max_length=15L)
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'tracking_bannedip'

class TrackingClicktrack(models.Model):
    id = models.IntegerField(primary_key=True)
    visitor_id = models.IntegerField(null=True, blank=True)
    user_agent = models.CharField(max_length=255L, blank=True)
    referer = models.CharField(max_length=255L, blank=True)
    target_url = models.CharField(max_length=255L, blank=True)
    source_url = models.CharField(max_length=255L, blank=True)
    source_url_type = models.CharField(max_length=10L, blank=True)
    merchant_domain = models.CharField(max_length=255L, blank=True)
    merchant_id = models.IntegerField(null=True, blank=True)
    coupon_id = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    acquisition_source = models.CharField(max_length=255L)
    acquisition_medium = models.CharField(max_length=255L)
    acquisition_term = models.CharField(max_length=255L)
    acquisition_content = models.CharField(max_length=255L)
    acquisition_campaign = models.CharField(max_length=255L)
    acquisition_gclid = models.CharField(max_length=255L)
    class Meta:
        db_table = 'tracking_clicktrack'

class TrackingCommission(models.Model):
    id = models.IntegerField(primary_key=True)
    commissionid = models.CharField(max_length=255L, unique=True, db_column='commissionID', blank=True) # Field name made lowercase.
    commissiontype = models.CharField(max_length=255L, db_column='commissionType', blank=True) # Field name made lowercase.
    commissionvalue = models.FloatField(db_column='commissionValue') # Field name made lowercase.
    currency = models.CharField(max_length=10L, blank=True)
    customid = models.CharField(max_length=50L, db_column='customID', blank=True) # Field name made lowercase.
    date = models.DateField(null=True, blank=True)
    domainid = models.CharField(max_length=255L, db_column='domainID', blank=True) # Field name made lowercase.
    merchantid = models.CharField(max_length=255L, db_column='merchantID', blank=True) # Field name made lowercase.
    publisherid = models.CharField(max_length=255L, db_column='publisherID', blank=True) # Field name made lowercase.
    items = models.IntegerField()
    sales = models.IntegerField()
    remotereferer = models.TextField(db_column='remoteReferer') # Field name made lowercase.
    remoteuseragent = models.TextField(db_column='remoteUserAgent') # Field name made lowercase.
    url = models.CharField(max_length=255L, blank=True)
    domain = models.CharField(max_length=255L, blank=True)
    status = models.CharField(max_length=255L, blank=True)
    customidasint = models.IntegerField(null=True, db_column='customIDAsInt', blank=True) # Field name made lowercase.
    ordervalue = models.FloatField(db_column='orderValue') # Field name made lowercase.
    class Meta:
        db_table = 'tracking_commission'

class TrackingRevenuevisitor(models.Model):
    id = models.IntegerField(primary_key=True)
    visitor_id = models.IntegerField(null=True, blank=True)
    session_key = models.CharField(max_length=40L)
    ip_address = models.CharField(max_length=20L)
    user_id = models.IntegerField(null=True, blank=True)
    user_agent = models.CharField(max_length=255L)
    referrer = models.CharField(max_length=255L)
    url = models.CharField(max_length=255L)
    page_views = models.IntegerField()
    session_start = models.DateTimeField()
    last_update = models.DateTimeField()
    acquisition_source = models.CharField(max_length=255L)
    acquisition_medium = models.CharField(max_length=255L)
    acquisition_term = models.CharField(max_length=255L)
    acquisition_content = models.CharField(max_length=255L)
    acquisition_campaign = models.CharField(max_length=255L)
    acquisition_gclid = models.CharField(max_length=255L)
    past_acquisition_info = models.TextField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    date_obj_added = models.DateTimeField()
    last_obj_modified = models.DateTimeField()
    class Meta:
        db_table = 'tracking_revenuevisitor'

class TrackingUntrackeduseragent(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=100L)
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'tracking_untrackeduseragent'

class TrackingVisitor(models.Model):
    id = models.IntegerField(primary_key=True)
    session_key = models.CharField(max_length=40L)
    ip_address = models.CharField(max_length=20L)
    user_id = models.IntegerField(null=True, blank=True)
    user_agent = models.CharField(max_length=255L)
    referrer = models.CharField(max_length=255L)
    url = models.CharField(max_length=255L)
    page_views = models.IntegerField()
    session_start = models.DateTimeField()
    last_update = models.DateTimeField()
    acquisition_source = models.CharField(max_length=255L)
    acquisition_medium = models.CharField(max_length=255L)
    acquisition_term = models.CharField(max_length=255L)
    acquisition_content = models.CharField(max_length=255L)
    acquisition_campaign = models.CharField(max_length=255L)
    acquisition_gclid = models.CharField(max_length=255L)
    past_acquisition_info = models.TextField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'tracking_visitor'

class WebFeaturedcoupon(models.Model):
    id = models.IntegerField(primary_key=True)
    coupon_id = models.IntegerField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'web_featuredcoupon'

class WebNewcoupon(models.Model):
    id = models.IntegerField(primary_key=True)
    coupon_id = models.IntegerField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'web_newcoupon'

class WebPopularcoupon(models.Model):
    id = models.IntegerField(primary_key=True)
    coupon_id = models.IntegerField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'web_popularcoupon'

class WebShortenedurlcomponent(models.Model):
    id = models.IntegerField(primary_key=True)
    original_url = models.TextField()
    shortened_url = models.CharField(max_length=35L)
    class Meta:
        db_table = 'web_shortenedurlcomponent'

class WebsvcsEmailsubscription(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=255L)
    session_key = models.CharField(max_length=255L)
    email = models.CharField(max_length=255L)
    first_name = models.CharField(max_length=255L, blank=True)
    last_name = models.CharField(max_length=255L, blank=True)
    full_name = models.CharField(max_length=255L, blank=True)
    context = models.TextField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'websvcs_emailsubscription'

class WebsvcsImagestore(models.Model):
    id = models.IntegerField(primary_key=True)
    remote_url = models.CharField(max_length=255L)
    local_url = models.CharField(max_length=255L)
    source_user_id = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    class Meta:
        db_table = 'websvcs_imagestore'

class WebsvcsShortenedurl(models.Model):
    id = models.IntegerField(primary_key=True)
    original_url = models.TextField()
    shortened_url = models.CharField(max_length=40L)
    class Meta:
        db_table = 'websvcs_shortenedurl'

