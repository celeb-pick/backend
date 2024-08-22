def get_filtered_celebrities(queryset, query_params):
    category = query_params.get("celebrity_category")
    if category:
        queryset = queryset.filter(category=category)
    
    search = query_params.get("search")
    if search:
        queryset = queryset.filter(name__contains=search)
    
    return queryset