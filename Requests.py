"""
Запросы написаны не по порядку 
"""

Entry.object.filter(headline__startswith="Technology") #Все записи относящиеся к блогу "Technology"
 
Entry.object.all().filter(pub_date__month=4) #Записи опубликованныйе в апреле 
 
Entry.object.filter(body_text_icontains="Music").filter(pub_date__gt=2010) #Опубликованы позже 2010
 
Entry.object.filter(number_of_comments__gt=F("15")).filter(headline__startswith="Art") #Записи арт 
 
Entry.object.order_by()[:10].get() #10 последних