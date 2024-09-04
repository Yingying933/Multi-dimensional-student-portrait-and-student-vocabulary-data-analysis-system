import os
import json

def init_json_data(schooltype, isSave=True):
    # 读取学生词汇量信息
    with open('./data/results.json', 'r', encoding='utf8') as sf:
        results_data = json.load(sf)
        sdict = {}  # {sid: [词汇量，测试字串]}
        for sattrs in results_data:
            sid = sattrs['xueshengbianhao']
            vocab = int(sattrs['chushixuexili'])
            if vocab > 0:
                sdict[sid] = [vocab]

    # 读取首测信息
    with open('.\\data\\exam.json', 'r', encoding='utf8') as examf:
        exam_data = json.load(examf)
        SIDList = []
        for sattrs in exam_data:
            sid = sattrs['xueshengbianhao']
            if sattrs['xueduan'] == schooltype and sid in sdict:
                # 读词汇表
                wordfile = '.\\data\\单词_' + schooltype + '.json'
                with open(wordfile, 'r', encoding='utf8') as wordf:
                    word_data = json.load(wordf)
                    worddict = {}  # {单词名称：单词id}
                    for wattrs in word_data:
                        worddict[wattrs['cihui']] = wattrs['cihuibianhao']

                examlist = ['0'] * 200
                if schooltype == '小学':
                    examlist = ['0'] * 164
                knowwords = sattrs['renshi'].split(' ')
                for w in knowwords:
                    if w in worddict:
                        examlist[int(worddict[w])] = '1'
                examstr = ''.join(examlist)
                sdict[sid].append(examstr)

    if isSave:
        testdir = '.\\data\\首测_单词_' + schooltype + '\\'
        if not os.path.exists(testdir):
            os.mkdir(testdir)

        for key in worddict.keys():
            fname = key + '_' + str(worddict[key]) + '.json'
            testfname = testdir + fname
            with open(testfname, 'w', encoding='utf8') as f:
                wstr = ''
                for k, v in sdict.items():
                    if len(v) == 2:
                        wstr += v[1][int(worddict[key])]  # 认识为1，不认识为0
                f.write(json.dumps(wstr))

                print(testfname, 'saved')

# 示例调用
init_json_data('小学')
