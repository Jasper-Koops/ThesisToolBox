from django.forms.models import model_to_dict

def source_dict_generator(linked_Tags, self):
    """
    :param linked_Tags:
    :return: A dict of both tags and a filtered list
    of the linked notes.
    """

    returndict = {}
    for tag in linked_Tags:
        hashed_tag = model_to_dict(tag)
        dict_list = [hashed_tag]
        notes = self.object.notes.filter(
            tags__id=tag.pk,
            user=self.request.user,
            object_id=self.object.pk,
        )
        for note in notes:
            tag_list = []
            for tag in note.tags.all():
                tag_list.append({
                    'id': tag.pk,
                    'name': tag.name
                })
            dict_model = model_to_dict(note)
            dict_model['linked_tags'] = tag_list
            dict_list.append(dict_model)
        returndict[tag] = dict_list
    return returndict


def tag_dict_generator(linked_Sources, self):
    """
    :param linked_Sources:
    :return: A dict of both sources and a filtered list
    of the linked notes.
    """
    returndict= {}
    for source in linked_Sources:
        hashed_source = model_to_dict(source)
        hashed_source['hashed_author'] = {
            'id': source.author.pk,
            'name': source.author.full_name,
        }
        dict_list = [hashed_source]
        notes = source.notes.filter(
            tags__id=self.object.pk,
            user=self.request.user
        )
        for note in notes:
            tag_list = []
            for tag in note.tags.all():
                tag_list.append({
                    'id': tag.pk,
                    'name': tag.name
                })
            dict_model = model_to_dict(note)
            dict_model['linked_tags'] = tag_list
            dict_list.append(dict_model)
        returndict[source] = dict_list

    return returndict
