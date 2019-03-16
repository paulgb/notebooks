{%- extends 'basic.tpl' -%}

{% block header %}
<!DOCTYPE html>
<html>
<head>
    <title>{{nb.metadata['title']}}</title>
    <link rel="stylesheet" href="/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Cabin:700|PT+Serif:400,400i,700" rel="stylesheet">
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration -->
</head>
{% endblock header %}

{% block body %}
<body>
    <div class="content">
        <div class="post">
        <h1><a href="/{{nb.metadata['path']}}/">{{nb.metadata['title']}}</a></h1>
        <p class="meta"><a href="https://paulbutler.org">Paul Butler</a> &ndash; {{nb.metadata['human_date']}}</p>

        <p class="notice">This post is also available as a Jupyter notebook.
        You can <a href="{{nb.metadata['notebook_path']}}">download it</a> or
        <a href="{{nb.metadata['binder_url']}}">run it on Binder</a> or
        <a href="{{nb.metadata['colab_url']}}">Colaboratory</a>.</p>
        
        <div class="postbody">
        {{ super() }}
        </div>

        <hr />

        <p>
            If you would like to be notified of future posts, you can
            <a href="https://twitter.com/paulgb">follow me on Twitter</a>
            or
            <a href="https://tinyletter.com/paulgb">subscribe to my occasional emails</a>.
        </p>
        </div>
    </div>
</body>
{% endblock body %}

{% block footer %}
</html>
{% endblock footer %}