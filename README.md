# Ex.05 Design a Website for Server Side Processing
## Date:03/12/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>Power Of a Lamp Filament</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style type="text/css">
body {
    background-color: rgb(222, 222, 0);
}
.edge {
    width: 100%;
    padding-top: 250px;
    text-align: center;
}
.box {
    display: inline-block;
    border: thick dashed rgb(255, 255, 255);
    width: 500px;
    min-height: 300px;
    font-size: 20px;
    background-color: rgb(0, 85, 255);
}
.formelt {
    color: rgb(255, 0, 0);
    text-align: center;
    margin-top: 7px;
    margin-bottom: 6px;
}
h1 {
    color: rgb(255, 245, 245);
    padding-top: 20px;
}
</style>
</head>
<body>
<div class="edge">
    <div class="box">
        <h1>power of a lamp filament </h1>
        <h3>THAVANESH(24900957)</h3>
        <form method="POST">
            {% csrf_token %}
            <div class="formelt">
                Intensity: <input type="text" name="intensity" value="{{i}}">m<br/>
            </div>
            <div class="formelt">
                Resistance: <input type="text" name="resistance" value="{{r}}">m<br/>
            </div>
            <div class="formelt">
                <input type="submit" value="Calculate"><br/>
            </div>
            <div class="formelt">
                Power: <input type="text" name="power" value="{{power}}">m<sup>2</sup><br/>
            </div>
        </form>
    </div>
</div>
</body>
</html>

views.py

from django.shortcuts import render

def power(request):
    context = {
        'power': "0",
        'r': "0",
        'h': "0"
    }
    if request.method == 'POST':
        print("POST method is used")
        i = request.POST.get('intensity', '0')
        r = request.POST.get('resistance', '0')
        
        try:
            intensity = float(i)
            resistance = float(r)
            
            power = (intensity ** 2) * resistance

            context['power'] = round(power, 2)
            context['i'] = i
            context['r'] = r
            print('intensity =', intensity)
            print('resistance =', resistance)
            print('power =', power)
        except ValueError:
            context['power'] = "Invalid input"
            print("Invalid input provided")
            
    return render(request, 'mathapp/math.html', context)

    urls.py

    from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerofbulb/',views.power,name="powerofbulb"),
    path('',views.power,name="power of bulb")
]


```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot (45).png>)


## HOMEPAGE:
![alt text](<Screenshot (44).png>)

## RESULT:
The program for performing server side processing is completed successfully.
