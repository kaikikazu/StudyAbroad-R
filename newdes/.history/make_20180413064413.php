<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>sample</title>
</head>
<body>
<p><?php

if(exec('python TwiPy.py') == 0){
    echo "SUCCESS!";
}else{
    echo "FALSE"
}

?></p>
<a href="output.csv">output.csv</a>
<a href="index2.html">index2.html</a>
<a href="form.html">戻る</a>
</body>
</html>