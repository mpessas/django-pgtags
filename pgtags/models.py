# -*- coding: utf-8 -*-

class TagsQuerySetMixin(object):
    """Mixin for querysets that have to query against tags."""

    tags_column_name = 'tags'

    def with_tags(self, tags):
        """Filter by the specified tags."""
        col_name = '"%s"."%s"' % (self.model._meta.db_table, self.tags_column_name)
        query = col_name + ' @> %s::varchar[]'
        return self.extra(where=[query, ], params=[tags])
