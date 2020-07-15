##TO DO

home: models.py
-----Add choices to Category class title field

home: templates/home.html ++ templates/detail.html

{% recursetree all_categories %}
<li>
 <a href="{% url 'home:path_to_products_by_category' node.slug %}">{{ node.title }}</a>
 {% if not node.is_leaf_node %}
	 <ul class="children">
	 	 {{ children }}
	 </ul>
 {% endif %}
</li>
{% endrecursetree %}

--------------REVIEW: NO results from root nodes | only children at the end of the tree produce lists