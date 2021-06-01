import random as rd

def predict_popularity(accessed_files, deleted_files, popularity,block_numbers, l, c, s, Pmin, Pmax):
    P = {}
    IP = 0
    Pred = {}
    avg_popularity = find_average_popularity(popularity)
    for f in set(accessed_files):
        P[f] = [0]
        
    for k in range(0, len(accessed_files)-1):
        f = accessed_files[k]
        i = len(P[f])-1
        
        if(i==0):
            P[f].append(avg_popularity)
            continue
        
        else:
            a = find_access_interval(f,k,accessed_files)
            b = find_block_numbers(f, block_numbers)
            calc = P[f][i] + c / (a*b*l*P[f][i])
            P[f].append(calc)
            
        if(P[f][i]<Pmin):
            P[f][i] = Pmin 
                    
        if(P[f][i]>Pmax):           
            P[f][i] = Pmax 
        
        IP = IP + P[f][i+1] - P[f][i]
                
    for f in deleted_files:
        #avg = find_average_popularity(popularity)
        IP = IP + avg_popularity - popularity[f]
        del P[f]
        del popularity[f]
        del block_numbers[f]
        
    MIP = IP / len(P)
 
    for f in P:
        i = len(P[f]) - 1
        P[f][i] = P[f][i] - MIP/s
        Pred[f] = P[f][i] + popularity[f]
        popularity[f] = P[f][i]          
        
    
    return Pred
 
#--------------------------HELPER FUNCTIONS-----------------------------        
def find_average_popularity(popularity):
    sum = 0
    for f in popularity:
        sum = sum + popularity[f]
        
    return sum/len(popularity)


def find_access_interval(f,k,files):
    key = accessed_files[k]
    k -= 1
    count  =  1
    while(k>=0):
        if(key==files[k]):
            break
        k -= 1
        count += 1
        
    return count * 10

def find_block_numbers(f, block_number):
    return block_number[f]

#==========================FOR PRINTING==============================
def print_popularity(popularity, block_numbers):
    print("Files \t\t Popularity \t Number_of_blocks")
    print("-----------------------------------------------")
    for f in popularity:
        print("file", f, ":\t", round(popularity[f],3),"\t\t", block_numbers[f] )
        
        
def print_predicted_popularity(pred):
    print("Files \t\t Predicted_Popularity")
    print("------------------------------------")
    for f in pred:
        print("file", f, ":\t", round(pred[f],3))
    
    
# =========================SIMULATION FUNCTIONS===================================
def simulate_popularity(accessed_files, Pmin, Pmax):
    p = {}
    for f in set(accessed_files):
        p[f] = rd.uniform(Pmin, Pmax)
        
    return p
        
        
def simulate_block_number(accessed_files, Bmin, Bmax):
    b = {}
    for f in set(accessed_files):
        b[f] = rd.randint(Bmin, Bmax)
        
    return b

def simulate_deleted_files(accessed_files):
    deleted = set()
    files = list(set(accessed_files))
    n = rd.randint(1, int(len(files)/3) + 1)
    for i in range(0, n):
        x = rd.choice(files)
        deleted.add(x)
        
    return deleted       

def simulate_accessed_files(number_of_files): 
    accessed_files = []
    n = rd.randint(number_of_files+5, 2 * number_of_files)
    for i in range(0, n):
        accessed_files.append(rd.randint(1, number_of_files))
        
    return accessed_files

#============================SIMULATION============================
Pmin = 0.1
Pmax = 0.9
accessed_files = simulate_accessed_files(9)
popularity = simulate_popularity(accessed_files, Pmin, Pmax)
Bmin = 1
Bmax = 50
block_numbers = simulate_block_number(accessed_files, Bmin, Bmax)
c = 10000
l = 9
s = 5
print_popularity(popularity, block_numbers)
print()
print("Accessing files: ", accessed_files)
deleted_files = list(simulate_deleted_files(accessed_files))
print("Deleting files: ", deleted_files)
print()
pred = predict_popularity(accessed_files, deleted_files, popularity,block_numbers, l, c, s, Pmin, Pmax)
print()
print_predicted_popularity(pred) 

 
    
    
    
    
    