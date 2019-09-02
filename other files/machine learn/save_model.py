from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import matthews_corrcoef
from sklearn.neighbors import KNeighborsClassifier 
import pandas as pd
from pandas import Series,DataFrame
from sklearn.externals import joblib

score_col = ['SIFT_score','Polyphen2_HDIV_score','Polyphen2_HVAR_score','LRT_score_new','MutationTaster_score_new','MutationAssessor_score','FATHMM_score','GERP++_RS',\
'PROVEAN_score','VEST3_score','MetaSVM_score','MetaLR_score','M-CAP_score','REVEL_score','MutPred_score','CADD_phred','DANN_score','fathmm-MKL_coding_score','Eigen-raw',\
'Eigen-PC-raw','GenoCanyon_score','SiPhy_29way_logOdds','integrated_fitCons_score','GM12878_fitCons_score','H1-hESC_fitCons_score','HUVEC_fitCons_score',\
'phyloP100way_vertebrate','phyloP20way_mammalian','phastCons100way_vertebrate','phastCons20way_mammalian','FATHMM_Cancer_score']
#print(len(score_col))

def knn_work(train_set, test_set,n,imp_feature):
    score_col = ['SIFT_score','Polyphen2_HDIV_score','Polyphen2_HVAR_score','LRT_score_new','MutationTaster_score_new','MutationAssessor_score','FATHMM_score','GERP++_RS',\
    'PROVEAN_score','VEST3_score','MetaSVM_score','MetaLR_score','M-CAP_score','REVEL_score','MutPred_score','CADD_phred','DANN_score','fathmm-MKL_coding_score','Eigen-raw',\
    'Eigen-PC-raw','GenoCanyon_score','SiPhy_29way_logOdds','integrated_fitCons_score','GM12878_fitCons_score','H1-hESC_fitCons_score','HUVEC_fitCons_score',\
    'phyloP100way_vertebrate','phyloP20way_mammalian','phastCons100way_vertebrate','phastCons20way_mammalian']
    best_list = ['MutPred_score','FATHMM_score','MetaLR_score','REVEL_score','MetaSVM_score','M-CAP_score','MutationAssessor_score','SiPhy_29way_logOdds','VEST3_score',\
                 'GERP++_RS','HUVEC_fitCons_score','PROVEAN_score','GM12878_fitCons_score','DANN_score','fathmm-MKL_coding_score']
    
    cnn_best = ['MutPred_score', 'MetaLR_score', 'REVEL_score', 'MetaSVM_score', 'M-CAP_score', \
            'MutationAssessor_score', 'DANN_score', 'HUVEC_fitCons_score', 'GM12878_fitCons_score', \
            'H1-hESC_fitCons_score', 'phyloP20way_mammalian', 'LRT_score_new', 'phastCons20way_mammalian']
    
    
    knn=KNeighborsClassifier(n_neighbors=n,n_jobs=-1)
    rf_best = ['MutPred_score', 'FATHMM_score', 'MetaLR_score', 'REVEL_score', 'MetaSVM_score', 'M-CAP_score', \
           'MutationAssessor_score', 'GERP++_RS', 'DANN_score', 'HUVEC_fitCons_score', 'GM12878_fitCons_score', \
           'H1-hESC_fitCons_score', 'phastCons20way_mammalian', 'GenoCanyon_score', 'phastCons100way_vertebrate']
    knn_799_best =['MutPred_score', 'FATHMM_score', 'MutationAssessor_score', 'VEST3_score', 'Eigen-PC-raw', \
            'H1-hESC_fitCons_score', 'MutationTaster_score_new']

    cnn_best.append('CHASMplus')
    knn_back = ['MutPred_score', 'FATHMM_score', 'M-CAP_score', 'MutationAssessor_score', 'VEST3_score',\
     'GM12878_fitCons_score', 'Eigen-raw', 'H1-hESC_fitCons_score']
    #knn_back.append('CHASMplus')
    t1 = ['MutPred_score', 'MutationAssessor_score', 'integrated_fitCons_score', 'phyloP20way_mammalian', \
     'phastCons20way_mammalian', 'CHASMplus', 'FATHMM_Cancer_score']
    cheat = ['FATHMM_score', 'REVEL_score', 'phyloP100way_vertebrate', 'fathmm-MKL_coding_score',\
             'PROVEAN_score', 'GM12878_fitCons_score', 'H1-hESC_fitCons_score', 'Polyphen2_HVAR_score',\
             'MutationTaster_score_new', 'LRT_score_new', 'phastCons20way_mammalian', 'GenoCanyon_score',\
             'phastCons100way_vertebrate', 'CHASMplus']
    chasm_train =   ['SIFT_score', 'FATHMM_score', 'VEST3_score', 'DANN_score',\
     'SiPhy_29way_logOdds', 'integrated_fitCons_score', 'HUVEC_fitCons_score']
    chasm_70_hit =  ['VEST3_score', 'M-CAP_score', 'integrated_fitCons_score',\
                     'GM12878_fitCons_score', 'H1-hESC_fitCons_score', 'HUVEC_fitCons_score']
    chasm_70_hit_149 =  ['MutationAssessor_score', 'GERP++_RS', 'VEST3_score', 'MetaSVM_score',\
                         'MetaLR_score', 'M-CAP_score', 'CADD_phred', 'integrated_fitCons_score',\
                         'GM12878_fitCons_score', 'H1-hESC_fitCons_score', 'HUVEC_fitCons_score']

    #cnn_best.append('FATHMM_Cancer_score')
    
    train_set_label = train_set['label']
    train_set_X = z_score(train_set[imp_feature])[imp_feature]
    test_set_label = test_set['label']
    test_set_X = z_score(test_set[imp_feature])[imp_feature]
    
    knn_X = knn.fit(train_set_X,train_set_label)
    joblib.dump(knn_X, 'knn_799_4_features.pkl')
    print(knn_X)
    '''
    print('begin predict')
    r = knn.predict(test_set_X)
    rr= knn.predict_proba(test_set_X)
    print('predict end')
    knn_score_for_z_score = knn.predict_proba(train_set_X)
    
    knn_result = []
    knn_result_for_z = []
    for pred in r:
        knn_result.append(pred)
    knn_pred = []
    for j in rr:
        knn_pred.append(j[1])
    for k in knn_score_for_z_score:
        knn_result_for_z.append(k[1])
        
    #print(r)
    #print(knn_result)
    FATHMM_Cancer_score = test_set.loc[:,'FATHMM_Cancer_score'] 
    CHASMplus = test_set.loc[:,'CHASMplus']
    #print(CHASMplus.name)
    ParsSNP = test_set.loc[:,'ParsSNP']
    c_result = cutoff(CHASMplus)
    p_result = cutoff(ParsSNP)
    vote_result = []
    for i in range(len(r)):
        if c_result[i] + p_result[i] + knn_result[i] >1:
            vote_result.append(1)
        else:
            vote_result.append(0)
    knn_pred = pd.Series(knn_pred)
    knn_pred.name = "knn"
    knn_result_for_z = pd.Series(knn_result_for_z)
    knn_result_for_z.name = "knn"

    k_z = z_score_list_debug(knn_pred,knn_result_for_z)
    c_z = z_score_list_debug(CHASMplus,train_set['CHASMplus'] )
    p_z = z_score_list_debug(ParsSNP,train_set['ParsSNP'])
    
    vote_score = []
    #print(k_z)
    #print(k_z)
    #print(p_z)
    for i in range(len(r)):
        #vote_score.append(0.5*k_z[i]+c_z[i]+0.5*p_z[i])
        vote_score.append(k_z[i]+c_z[i]+p_z[i])
    #save_score(CHASMplus,ParsSNP,vote_score,knn_pred)
    vote_score = pd.Series(vote_score)
    vote_score.name = "vote_score"    
    print(type(test_set_label))
    temp_result = pd.concat([CHASMplus,ParsSNP,vote_score,knn_pred,test_set_label], axis=1)
    temp_file_name = 'combine_cancer_score_from_hpm_exac_debug_' +str(len(imp_feature)) +'.csv'
    temp_result.to_csv(temp_file_name,index=0)
    roc(test_set_label,CHASMplus,ParsSNP,vote_score,imp_feature)  
    

    
    
            
                
            
    #print(c_result)
    
    
    #mcc = matthews_corrcoef(test_set_label, r)
    #acc = accuracy_score(test_set_label, r)
    #roc(test_set_label,FATHMM_Cancer_score,CHASMplus,score_pred)
	'''
    return 1,1
def cutoff(x):
    score_name = x.name
    cutoff_dict =  {'FATHMM_score': -1.5, 'integrated_fitCons_score': 0.7, 'GM12878_fitCons_score': 0.7, 'H1.hESC_fitCons_score': 0.7, 'HUVEC_fitCons_score': 0.7, 'LRT_score_new': 0.999, \
    'MutationAssessor_score': 1.9, 'MutationTaster_score_new': 0.5, 'Polyphen2_HDIV_score': 0.453, 'Polyphen2_HVAR_score': 0.447, 'PROVEAN_score': 2.5, 'SIFT_score': 0.95, 'VEST3_score': 0.5, \
    'MutPred_score': 0.5, 'GERP.._RS': 2.0, 'phyloP100way_vertebrate': 2.0, 'phyloP20way_mammalian': 2.0, 'phastCons100way_vertebrate': 0.999, 'phastCons20way_mammalian': 0.999, 'SiPhy_29way_logOdds': 12.0, \
    'CADD_phred': 20.0, 'DANN_score': 0.99, 'Eigen.raw': 0.0, 'Eigen.PC.raw': 0.0, 'fathmm.MKL_coding_score': 0.5, 'GenoCanyon_score': 0.999, 'M.CAP_score': 0.025, 'MetaLR_score': 0.5, 'MetaSVM_score': 0.0, 'REVEL_score': 0.4, \
    'CHASMplus': 0.279, 'FATHMM_Cancer_score': 0.75, 'CanDrA_Score': 0.15, 'ParsSNP': 0.07, 'CONDEL': 0.522}
    pred_list = []
    cutoff_temp = cutoff_dict[score_name]
    for i in x:
        if i > cutoff_temp:
            pred_list.append(1)
        else:
            pred_list.append(0)
    return pred_list


def roc(label,score1,score2,score3,imp):
    fpr1, tpr1, _ = roc_curve(label, score1)
    roc_auc1 = auc(fpr1, tpr1)
    fpr2, tpr2, _ = roc_curve(label, score2)
    roc_auc2 = auc(fpr2, tpr2)
    fpr3, tpr3, _ = roc_curve(label, score3)
    roc_auc3 = auc(fpr3, tpr3)
    
    plt.figure()
    
    plt.plot(fpr1, tpr1, color='navy', lw=2, label='CHASMplus ROC curve (area = %0.2f)' % roc_auc1)
    plt.plot(fpr2, tpr2, color='yellow', lw=2, label='ParsSNP ROC curve (area = %0.2f)' % roc_auc2)
    plt.plot(fpr3, tpr3, color='red', lw=2, label='vote score ROC curve (area = %0.2f)' % roc_auc3)
    plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
    '''
    plt.plot(fpr1, tpr1, color='navy', lw=2, label='FATHMM_Cancer_score ROC ' )
    plt.plot(fpr2, tpr2, color='yellow', lw=2, label='CHASMplus')
    plt.plot(fpr3, tpr3, color='red', lw=2, label='new score')
    #plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
    print('auc = ',roc_auc3)
    #plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    '''
    plt.xlim([0.0, 1])
    plt.ylim([0.0, 1.00])
    plt.xlabel('False Positive Rate') 
    plt.ylabel('True Positive Rate')
    plt.title(str(imp))
    plt.legend(loc="lower right")
    plt.show()    
def z_score(X):
    z_list = []
    z_list = pd.Series(z_list)
    for i in range(X.shape[1]):
        a = X.iloc[:, [i]]
        a_mean = a.mean(axis=0)  
        a_std = a.std(axis=0)  
        a1 = (a-a_mean)/a_std
        z_list = pd.concat([z_list,a1],axis=1)
        #print(z_list)
    #z_list = z_list.iloc[:,[1,z_list.shape[1]-1]]
    return z_list
def z_score_list(X):
    z_list = []
    z_list = pd.Series(z_list)
    for i in range(1):
        a = X
        a_mean = a.mean(axis=0)  
        a_std = a.std(axis=0)  
        a1 = (a-a_mean)/a_std
        z_list = pd.concat([z_list,a1],axis=1)
        #print(z_list)
    #z_list = z_list.iloc[:,[1,z_list.shape[1]-1]]
    return z_list
def z_score_list_debug(X,base):
    #print(X.index)
    Y = []
    b = base
    z_list = []
    z_list = pd.Series(z_list)
    b_mean = b.mean(axis=0)
    b_std = b.std(axis=0)
    for index in X.index:
        #print(X[index])
        #mean &std
        
        Y.append((X[index]-b_mean)/b_std)

        #print(z_list)
    #z_list = z_list.iloc[:,[1,z_list.shape[1]-1]]
    Y=  pd.Series(Y)
    print(X.name)

    Y.name = X.name
    #print(Y)
    print(X.name,b_mean,b_std)
    return Y
    
ss = ShuffleSplit(n_splits=1, random_state=0, test_size=0.10)
tr_vote_new = pd.read_csv('/home/web/public/data/projects/varientDB/database/model/fathmm_train_final.csv')
tr_vote_new = DataFrame(tr_vote_new)


te_set2 = pd.read_csv('/home/web/public/data/projects/varientDB/database/model/fmd_fmn_have_all_score_del_chasmplus_fathmmcancer_parssnp_training_set.tsv', sep='\t')
te_set2 = DataFrame(te_set2)


'''
te_set6 = pd.read_csv('/data/wangs/MutaAnalysis/three.data0223/output/findal/drop.all.training/hpm_hpmrandom_have_all_score_del_chasmplus_fathmmcancer_parssnp_training_set.tsv', sep='\t')
te_set6 = DataFrame(te_set6)
'''
imp_list = []
imp = ['MutationAssessor_score', 'VEST3_score', 'MetaSVM_score', 'M-CAP_score', 'REVEL_score', 'MutPred_score', 'CADD_phred', 'GERP++_RS', 'SiPhy_29way_logOdds', 'CONDEL', 'FATHMM_score']
#imp_list.append(imp)

imp =['VEST3_score', 'MutPred_score', 'GERP++_RS', 'FATHMM_score']
imp_list.append(imp)

print(imp_list)
#te_fmd_exac =pd.read_csv('/data/wangs/MutaAnalysis/three.data0223/output/findal/drop.all.training/fmd_exac_have_all_score_del_chasmplus_fathmmcancer_parssnp_training_set.tsv', sep='\t')
#te_fmd_exac = DataFrame(te_fmd_exac)
#te_fmd_exac_pos = te_fmd_exac[te_fmd_exac['label'] == 1]
#print(te_fmd_exac_pos)

for imp in imp_list:
    n = 799
    print('n_neighbors = ',n)
    
    mcc,acc = knn_work(tr_vote_new,te_set2,n,imp)
    #acc_list.append(acc)

    
    #print('acc = ',acc)  
    #print('mcc = ',mcc)
cutoff_dict =  {'FATHMM_score': -1.5, 'integrated_fitCons_score': 0.7, 'GM12878_fitCons_score': 0.7, 'H1.hESC_fitCons_score': 0.7, 'HUVEC_fitCons_score': 0.7, 'LRT_score_new': 0.999, 'MutationAssessor_score': 1.9, 'MutationTaster_score_new': 0.5, 'Polyphen2_HDIV_score': 0.453, 'Polyphen2_HVAR_score': 0.447, 'PROVEAN_score': 2.5, 'SIFT_score': 0.95, 'VEST3_score': 0.5, 'MutPred_score': 0.5, 'GERP.._RS': 2.0, 'phyloP100way_vertebrate': 2.0, 'phyloP20way_mammalian': 2.0, 'phastCons100way_vertebrate': 0.999, 'phastCons20way_mammalian': 0.999, 'SiPhy_29way_logOdds': 12.0, 'CADD_phred': 20.0, 'DANN_score': 0.99, 'Eigen.raw': 0.0, 'Eigen.PC.raw': 0.0, 'fathmm.MKL_coding_score': 0.5, 'GenoCanyon_score': 0.999, 'M.CAP_score': 0.025, 'MetaLR_score': 0.5, 'MetaSVM_score': 0.0, 'REVEL_score': 0.4, 'CHASMplus': 0.279, 'FATHMM_Cancer_score': 0.75, 'CanDrA_Score': 0.15, 'ParsSNP': 0.07, 'CONDEL': 0.522}

