# Lando

L - Lazy (least amount of work )  
A - Austere (simple)  
N - Naked (vanilla JS only!)  
D - Dandy (is fun! )  
O - Optimized (is fast! )  



## What is LANDO

Lando isn't a javascript library rather it is a framework to keep apps simple, straight forward, and easy to develop on. Land uses vanilla JS to deliver blazing fast apps, without the need for web pack, other libraries or any sort of complexity. LANDO apps live directly in the back end app , and are compiled in the browser only when the user needs it .

### 1. LANDO in action

LANDO can integrate with any backend frameworks. This example is in django. Say, we want to dynamically change the prices on a products page. With LANDO you can just write:

```
{% for object in object_list %}


function increasePrice_{{object.pk}}() {

  document.getElementById("product_{{object.pk}}").innerHTML = parseInt(document.getElementById("product_{{object.pk}}").innerHTML) + 2;

}
{% endfor %}
```

Which when the browser loads turns into:

```

    function increasePrice_1() {

      document.getElementById("product_1").innerHTML = parseInt(document.getElementById("product_1").innerHTML) + 2;

    }



    function increasePrice_2() {

      document.getElementById("product_2").innerHTML = parseInt(document.getElementById("product_2").innerHTML) + 2;

    }
.....
```

Which in two lines of code handles all of hte changing of any product pricing on the whole app. This is much simpler than react.js, svelte.js, or angular which requires massive bundling of dependancies and usage of n-th degrees of unknown libraries. LANDO is just javascript and as a result doesn't need any of that.     
