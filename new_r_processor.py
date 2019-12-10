import os
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import pandas as pd

rms = importr('rms')


class R_processor(object):
    def get_liner_predictor(self, x0, x1, y0, y1, total_points):
        a = (y0 - y1) / (x0 - x1)
        b = y0 - a * x0
        return a * total_points + b

    def os_processor(self, age, gender, alb, t_category, n_category):
        cur_path = os.path.dirname(os.path.abspath(__file__))

        para_trans = self.para_mapping(age=age, gender=gender, alb=alb,
                                       t_category=t_category, n_category=n_category)
        s = robjects.r("""
            f <- readRDS("{path}/model1/OSmodel")
            f=Newlabels(f,c(Tcategory="T stage",Node="N stage",ALB="ALB (g/L)")) 
            surv<-Survival(f)
            survest(f,expand.grid(Age="{a}",Gender="{b}",ALB="{c}",Tcategory="{e}",Node="{f}"),times=c(12, 24, 36, 48, 60))
            """.format(path=cur_path, a=para_trans["age"], b=para_trans["gender"], c=para_trans["alb"],
                       e=para_trans["t_category"], f=para_trans["n_category"]))

        # res = ['os',{"risk": s[1][0], "lower": s[3][0], "upper": s[4][0],
        #         "index": {"age": age, "gender": gender, "alb": alb,
        #                   "t_category": t_category, "n_category": n_category}, "real_para": para_trans},
        #        {"risk": s[1][1], "lower": s[3][1], "upper": s[4][1]},
        #        {"risk": s[1][2], "lower": s[3][2], "upper": s[4][2]},
        #        {"risk": s[1][3], "lower": s[3][3], "upper": s[4][3]},
        #        {"risk": s[1][4], "lower": s[3][4], "upper": s[4][4]}]
        res = [{"risk": s[1][0], "lower": s[3][0], "upper": s[4][0]},
               {"risk": s[1][1], "lower": s[3][1], "upper": s[4][1]},
               {"risk": s[1][2], "lower": s[3][2], "upper": s[4][2]},
               {"risk": s[1][3], "lower": s[3][3], "upper": s[4][3]},
               {"risk": s[1][4], "lower": s[3][4], "upper": s[4][4]}]

        return res

    def lrfs_processor(self, smoking_history, t_category, n_category):
        cur_path = os.path.dirname(os.path.abspath(__file__))

        para_trans = self.para_mapping(smoking_history=smoking_history, t_category=t_category, n_category=n_category)
        s = robjects.r("""
            f <- readRDS("{path}/model1/LRFSmodel")
            f=Newlabels(f,c(Tcategory="T stage",Node="N stage")) 
            surv<-Survival(f)       
            survest(f,expand.grid(Tcategory="{e}",Smoking="{g}",Node="{f}"),times=c(12, 24, 36, 48, 60))
            """.format(path=cur_path, e=para_trans["t_category"], g=para_trans["smoking_history"],
                       f=para_trans["n_category"]))

        res = [{"risk": s[1][0], "lower": s[3][0], "upper": s[4][0]},
               {"risk": s[1][1], "lower": s[3][1], "upper": s[4][1]},
               {"risk": s[1][2], "lower": s[3][2], "upper": s[4][2]},
               {"risk": s[1][3], "lower": s[3][3], "upper": s[4][3]},
               {"risk": s[1][4], "lower": s[3][4], "upper": s[4][4]}]

        return res

    def rrfs_processor(self, t_category, n_category):
        cur_path = os.path.dirname(os.path.abspath(__file__))

        para_trans = self.para_mapping(t_category=t_category, n_category=n_category)
        s = robjects.r("""
            f <- readRDS("{path}/model1/RRFSmodel")
            f=Newlabels(f,c(Tcategory="T stage",Node="N stage")) 
            surv<-Survival(f)      
            survest(f,expand.grid(Tcategory="{e}",Node="{f}"),times=c(12, 24, 36, 48, 60))
            """.format(path=cur_path, e=para_trans["t_category"],
                       f=para_trans["n_category"]))

        res = [{"risk": s[1][0], "lower": s[3][0], "upper": s[4][0]},
               {"risk": s[1][1], "lower": s[3][1], "upper": s[4][1]},
               {"risk": s[1][2], "lower": s[3][2], "upper": s[4][2]},
               {"risk": s[1][3], "lower": s[3][3], "upper": s[4][3]},
               {"risk": s[1][4], "lower": s[3][4], "upper": s[4][4]}]

        return res

    def dmfs_processor(self, age, gender, t_category, n_category):
        cur_path = os.path.dirname(os.path.abspath(__file__))

        para_trans = self.para_mapping(age=age, gender=gender, t_category=t_category, n_category=n_category)
        s = robjects.r("""
            f <- readRDS("{path}/model1/DMFSmodel")
            f=Newlabels(f,c(Tcategory="T stage",Node="N stage")) 
            surv<-Survival(f)
            survest(f,expand.grid(Age="{a}",Gender="{b}",Tcategory="{e}",Node="{f}"),times=c(12, 24, 36, 48, 60))
            """.format(path=cur_path, a=para_trans["age"], b=para_trans["gender"],
                       e=para_trans["t_category"], f=para_trans["n_category"]))

        res = [{"risk": s[1][0], "lower": s[3][0], "upper": s[4][0]},
               {"risk": s[1][1], "lower": s[3][1], "upper": s[4][1]},
               {"risk": s[1][2], "lower": s[3][2], "upper": s[4][2]},
               {"risk": s[1][3], "lower": s[3][3], "upper": s[4][3]},
               {"risk": s[1][4], "lower": s[3][4], "upper": s[4][4]}]

        return res

    def dfs_processor(self, age, gender, smoking_history, t_category, n_category):
        cur_path = os.path.dirname(os.path.abspath(__file__))

        para_trans = self.para_mapping(age=age, gender=gender, smoking_history=smoking_history, t_category=t_category,
                                       n_category=n_category)
        s = robjects.r("""
            f <- readRDS("{path}/model1/DFSmodel")
            f=Newlabels(f,c(Tcategory="T stage",Node="N stage")) 
            surv<-Survival(f)
            survest(f,expand.grid(Age="{a}",Gender="{b}",Smoking="{g}",Tcategory="{e}",Node="{f}"),times=c(12, 24, 36, 48, 60))
            """.format(path=cur_path, a=para_trans["age"], b=para_trans["gender"],
                       g=para_trans["smoking_history"],
                       e=para_trans["t_category"], f=para_trans["n_category"]))

        res = [{"risk": s[1][0], "lower": s[3][0], "upper": s[4][0]},
               {"risk": s[1][1], "lower": s[3][1], "upper": s[4][1]},
               {"risk": s[1][2], "lower": s[3][2], "upper": s[4][2]},
               {"risk": s[1][3], "lower": s[3][3], "upper": s[4][3]},
               {"risk": s[1][4], "lower": s[3][4], "upper": s[4][4]}]

        return res

    def para_mapping(self, age=None, gender=None, alb=None, who_pathology_type=None, t_category=None, n_category=None,
                     smoking_history=None):
        trans_dict = {"age": ["<30", "30-39", "40-49", "50-59", ">=60"],
                      "gender": ["Female", "Male"],
                      "alb": ["<40", ">40"],
                      "who_pathology_type": ["Type I-II", "Type III"],
                      "t_category": ["T1", "T2", "T3", "T4"],
                      "n_category": ["N0", "N1", "N2", "N3"],
                      "smoking_history": ["Yes", "No"]
                      }
        res = dict()
        if age is not None:
            res["age"] = trans_dict["age"][age]
        if gender is not None:
            res["gender"] = trans_dict["gender"][gender]
        if alb is not None:
            res["alb"] = trans_dict["alb"][alb]
        if who_pathology_type is not None:
            res["who_pathology_type"] = trans_dict["who_pathology_type"][who_pathology_type]
        if t_category is not None:
            res["t_category"] = trans_dict["t_category"][t_category]
        if n_category is not None:
            res["n_category"] = trans_dict["n_category"][n_category]
        if smoking_history is not None:
            res["smoking_history"] = trans_dict["smoking_history"][smoking_history]
        return res


if __name__ == '__main__':
    r_processor = R_processor()

    # age gender alb who_pathology_type t_category n_category smoking_history
    # 0-5 0-1    0-1 0-1                0-3        0-3        0-1

    ps=[[3, 1, 1, 1, 3, 1, 1],
    [2, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 3, 3, 0]]
    dfosl = pd.DataFrame(columns=["risk", "lower", "upper"])
    dflrfs = pd.DataFrame(columns=["risk", "lower", "upper"])
    dfrrfs = pd.DataFrame(columns=["risk", "lower", "upper"])
    dfdmfs = pd.DataFrame(columns=["risk", "lower", "upper"])
    dfdfs = pd.DataFrame(columns=["risk", "lower", "upper"])
    for i in range(len(ps)):
        p=ps[i]
        # age, gender, alb, t_category, n_category
        osl = r_processor.os_processor(p[0], p[1], p[2], p[4], p[5])
        df1 = pd.DataFrame(columns=["risk", "lower", "upper"])
        for a in range(5):
            # 循环将字典添加到空的dataframe
            df1 = df1.append(osl[a], ignore_index=True)
        dfosl = dfosl.append(df1)

        # smoking_history, t_category, n_category
        lrfs = r_processor.lrfs_processor(p[6], p[4], p[5])
        df2 = pd.DataFrame(columns=["risk", "lower", "upper"])
        for b in range(5):
            # 循环将字典添加到空的dataframe
            df2 = df2.append(lrfs[b], ignore_index=True)
        dflrfs = dflrfs.append(df2)

        # t_category, n_category
        rrfs = r_processor.rrfs_processor(p[4], p[5])
        df3 = pd.DataFrame(columns=["risk", "lower", "upper"])
        for c in range(5):
            # 循环将字典添加到空的dataframe
            df3 = df3.append(rrfs[c], ignore_index=True)
        dfrrfs = dfrrfs.append(df3)

        # age, gender, t_category, n_category
        dmfs = r_processor.dmfs_processor(p[0], p[1], p[4], p[5])
        df4 = pd.DataFrame(columns=["risk", "lower", "upper"])
        for d in range(5):
            # 循环将字典添加到空的dataframe
            df4 = df4.append(dmfs[d], ignore_index=True)
        dfdmfs = dfdmfs.append(df4)

        # age, gender, smoking_history, t_category, n_category
        dfs = r_processor.dfs_processor(p[0], p[1], p[6], p[4], p[5])
        df5 = pd.DataFrame(columns=["risk", "lower", "upper"])
        for e in range(5):
            # 循环将字典添加到空的dataframe
            df5 = df5.append(dfs[e], ignore_index=True)
        dfdfs = dfdfs.append(df5)
    print(dfosl,dflrfs,dfrrfs,dfdmfs,dfdfs)

