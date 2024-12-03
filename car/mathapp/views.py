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