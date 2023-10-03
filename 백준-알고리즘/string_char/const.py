n,m = input().split()
n_s = n[::-1]
m_s = m[::-1]
if n_s > m_s:
    print(n_s)
else:
    print(m_s)