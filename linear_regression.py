
import numpy as np
import matplotlib.pyplot as plt
def esti(x,y):
    n=np.size(x)
    
    m_x=np.mean(x)
    m_y=np.mean(y)
    
    ss_xy=np.sum(y*x)-n*m_x*m_y
    ss_xx=np.sum(x*x)-n*m_x*m_x
    
    b_1=ss_xy/ss_xx
    b_0=m_y-b_1*m_x
    
    return(b_0,b_1)
    
def prit(x,y,b):
    plt.scatter(x,y,color="red",mark="o")
    y_pred=b[0]+b[1]*x
    
    plt.plot(x,y_pred)
    
    plt.show()
    
    
def main():
    x=np.array([2,3,4,5,6,7,8,9])
    y=np.array([1,2,4,5,6,2,3,6])
    
    b=esti(x,y)
    print("coefficients are:".format(b[0],b[1]))
    prit(x,y,b)
    
if __name__=="__main__":
    main()
