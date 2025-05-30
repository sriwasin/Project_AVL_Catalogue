# Project_AVL_Catalogue

Hypothetical requirements:
<ul>
  <li>Client is looking for a system to help set up and manage a large catalogue of goods for their e-commerce website.</li>
  <li>They are looking for simple functionalities to add, remove, and lookup items within the database.</li>
  <li>The lookup will also serve the frontend when customers inquire for items. Thus, heavy lookup traffic is expected at all time.</li>
  <li>The catalogue is expected to host about 100,000 items and will be fairly static (i.e. add and remove operations will be limited and not be done by customers).</li>
  <li>For a well-functioning e-commerce website, client expects performance to be high. Customers must not experience any noticeably slow product searches.</li>
</ul>
  
Abstract:
<ul>
  <li>This project explores AVL as the fundamental data structure to support product cataloguing of an e-commerce site.</li>
  <li>Since AVL guarantees O(logn) time complexity, it is expected that the data structure will deliver favorable performance once it has to facilitate large product catalogue and high traffic from users.</li>
  <li>A combination of queue, stack and BST will be used to support AVL operations</li>
</ul>
  
Limitations:
<ul>
  <li>For the purpose of this exploration, we acknowledge that AVL may not be the most suitable data structure for e-commerce website with large number of items to manage in the database. That being said, the concept of self-balancing data structure that self-optimises performance is still sound and would apply here.</li>
  <li>We will omit construction of user interface, and simply induce that if the data structure performs well, it would reflect well on user experience (particularly on product lookup traffic)</li>
</ul>
