import re

html = """
<div class="product">
    <span class="price">$19.99</span>
    <span class="name">Product Name</span>
</div>
"""
price_pattern = r'<span class="price">\$(\d+\.\d{2})</span>'
name_pattern = r'<span class="name">([^<]+)</span>'
price = re.search(price_pattern, html).group(1)
name = re.search(name_pattern, html).group(1)
print(f"Product: {name}, Price: ${price}")