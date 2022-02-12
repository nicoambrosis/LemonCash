#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Este programita permite calcular a que precio devuelve el cash back Lemon cash.


# In[10]:


print("Ingresar el monto de la compra")
compra_ARS = float(input())

print("ingrese el monto de BTC recibido como cashback")
cashback_BTC = round((float(input())),9)

   


cashback_ARS = (2*compra_ARS)/100
btc_price = cashback_ARS/cashback_BTC

print('\n'*5)

print(f' GASTO = {int(compra_ARS):,} ARS '.center(50,'^'))

print(f' CASHBACK EN ARS = {cashback_ARS:.2f} ARS '.center(50,'^'))

print(f' CASHBACK en  BTC = {cashback_BTC:.8f} BTC '.center(50,'^'))

print(f' PRECIO BTC = {int(btc_price):,} ARS '.center(50,'^'))


print("\n"*5 + "NOTA: Separador de MILES: ,\n Separador de DECIMALES: .")


# In[ ]:




