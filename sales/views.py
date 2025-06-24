from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sale
from .forms import SalesSearchForm
from .utils import get_bookname_from_id, get_chart
import pandas as pd

def home(request):
    return render(request, 'sales/home.html')

@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)
    sales = Sale.objects.none()  # default empty queryset
    chart = None

    if request.method == 'POST' and form.is_valid():
        book_title = form.cleaned_data.get('book_title')
        chart_type = form.cleaned_data.get('chart_type')
        sales = Sale.objects.filter(book__name__icontains=book_title)

        if sales.exists():
            import pandas as pd
            sales_df = pd.DataFrame(sales.values())
            sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)
            chart = get_chart(chart_type, sales_df, labels=sales_df['date_created'].values)
        else:
            sales = Sale.objects.none()  # no sales found
    else:
        sales = Sale.objects.all()

    context = {
        'form': form,
        'sales': sales,   # pass queryset for template iteration
        'chart': chart,
    }
    return render(request, 'sales/records.html', context)
