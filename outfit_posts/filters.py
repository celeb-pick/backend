from .models import OutfitPost

def get_filtered_outfit_posts(queryset, query_params):
    gender = query_params.get("gender")
    if gender:
        queryset = queryset.filter(gender__in=[gender, OutfitPost.UNISEX])
    
    celebrity_category = query_params.get("celebrity_category")
    if celebrity_category:
        queryset = queryset.filter(celebrity__category=celebrity_category)
    
    search = query_params.get("search")
    if search:
        queryset = queryset.filter(title__contains=search)

    item_id = query_params.get("item_id")
    if item_id:
        queryset = queryset.filter(items__id=item_id)
    
    return queryset


def get_filtered_outfit_items(queryset, query_params):
    item_category = query_params.get("item_category")
    if item_category:
        queryset = queryset.filter(category=item_category)
    
    search = query_params.get("search")
    if search:
        queryset = queryset.filter(name__contains=search)
    
    return queryset
