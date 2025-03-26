import pandas as pd

data = pd.read_csv('C:/Users/amar/Desktop/iti/lab/New folder/Sales_April_2019.csv')


data_2 = data.drop_duplicates()


data_3 = data_2.dropna()
data_4 = data_3.dropna(subset=['Order Date'])
data_4['Order Date'] = pd.to_datetime(data_4['Order Date'], errors='coerce', format='%m/%d/%y %H:%M')

data_5 = data_4.astype({
    'Order ID': 'int32',
    'Product': 'string',
    'Quantity Ordered': 'int32',
    'Price Each': 'float32'
}, errors='ignore')


data_5['City'] = data_5['Purchase Address'].str.split(',').str[1].str.strip()
data_5['Purchase Address'] = data_5['Purchase Address'].str.split(',').str[0]

def clean_numeric(column):
    return (
        column.astype(str)
        .str.replace(r'[^\d.]', '', regex=True)  
        .replace('', '0')  
    )
data_5['Quantity Ordered'] = clean_numeric(data_5['Quantity Ordered']).astype('int32')
data_5['Price Each'] = clean_numeric(data_5['Price Each']).astype('float32')
data_5['Total'] = data_5['Quantity Ordered'] * data_5['Price Each']

data_5 = data_5.rename(columns={
    'Order ID': 'order_id',
    'Product': 'product_name',
    'Quantity Ordered': 'quantity',
    'Price Each': 'unit_price',
    'Order Date': 'order_date',
    'Purchase Address': 'purchase_address',
    'City': 'city',
    'Total': 'total_price'
})


data_5.to_csv('Sales_April_2019 after cleaning .csv', index=False)

