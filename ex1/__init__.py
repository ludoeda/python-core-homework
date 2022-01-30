def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    result = {}
    categories = []

    for categoryId in mapping['categoryIdsSorted']:
        rawCategoryValue = mapping['categories'][categoryId]
        roles = []
        
        for roleId in rawCategoryValue['roleIds']:
            role = {"id": roleId, "text": mapping['roles'][roleId]['name']}
            roles.append(role)

        category = {"id": f'category-{categoryId}', "text": rawCategoryValue['name'], "items": roles}
        categories.append(category)

    result['categories'] = categories

    return result
