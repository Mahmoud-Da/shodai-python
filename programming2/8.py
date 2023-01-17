#!/usr/bin/env python
# coding: utf-8

# # 2. 授業課題

# ### 1. 2^10 を計算し，計算結果を表示させよ
# ### (Hint: 累乗の演算子を使う)．
# ***

# In[2]:


a=2**10 # 2掛け１０
print(a)#結果を表示


# ### 2. a = "PYTHON" という文字列オブジェクトを，"python"という文字列に変換して表示させよ．
# ### (Hint:lower() というメソッドを使用せよ.)
# ***

# In[3]:


a = "PYTHON"
print(a.lower()) # {lower()}を追加して、大文字が小文字まで変化する


# ### 3. address = "東京都新宿区北新宿" という文字列オブジェクトとメソッド replace() を使って,
# ### 「東京都渋谷区原宿」と表示させよ．
# ***
# 

# In[4]:


address = "東京都新宿区北新宿"
new_address = address.replace("新宿区北新宿",'渋谷区原宿')#replceメソッドを追加をすると"新宿区北新宿"は'渋谷区原宿'に変化できる
print(new_address)#結果を表示


# ### 4. address = "東京都新宿区北新宿"という文字列から，インデックスを使って
# ### 「東」という文字列を表示させよ.
# ***
# 

# In[5]:


address = "東京都新宿区北新宿"
print(address[0]) #[]を追加すると言葉の順番を表示する

    


# ### 5. 音速 1225[km/h] をマッハ 1 と呼ぶ．
# ### 一方，光速  は 299792458 [m/s] である．
# ### では，光速はマッハいくつかを計算せよ．
# ### (マッハ◯◯の◯◯の 部分を最終的に表示させよ).
# ***

# In[6]:


light_speed = 299792458/1000#kmに変換
unite = ("マッハ")
result = 299792458*1/1225 #光速はマッハいくつかを計算する
print(result,unite)


# In[ ]:


