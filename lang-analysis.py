# -*- encoding: utf8 -*-
import csv
import langid
import re
from math import log
mycsv = open("instagram_shanghai_new.csv")
reader = csv.reader(x.replace('\0', '') for x in mycsv)
no_caption_csv = open('result2/no_caption_csv.csv','w')
af_csv = open('result2/af.csv','w')
am_csv = open('result2/am.csv','w')
an_csv = open('result2/an.csv','w')
ar_csv = open('result2/ar.csv','w')
as_csv = open('result2/as.csv','w')
az_csv = open('result2/az.csv','w')
be_csv = open('result2/be.csv','w')
bg_csv = open('result2/bg.csv','w')
bn_csv = open('result2/bn.csv','w')
br_csv = open('result2/br.csv','w')
bs_csv = open('result2/bs.csv','w')
ca_csv = open('result2/ca.csv','w')
cs_csv = open('result2/cs.csv','w')
cy_csv = open('result2/cy.csv','w')
da_csv = open('result2/da.csv','w')
de_csv = open('result2/de.csv','w')
dz_csv = open('result2/dz.csv','w')
el_csv = open('result2/el.csv','w')
en_csv = open('result2/en.csv','w')
eo_csv = open('result2/eo.csv','w')
es_csv = open('result2/es.csv','w')
et_csv = open('result2/et.csv','w')
eu_csv = open('result2/eu.csv','w')
fa_csv = open('result2/fa.csv','w')
fi_csv = open('result2/fi.csv','w')
fo_csv = open('result2/fo.csv','w')
fr_csv = open('result2/fr.csv','w')
ga_csv = open('result2/ga.csv','w')
gl_csv = open('result2/gl.csv','w')
gu_csv = open('result2/gu.csv','w')
he_csv = open('result2/he.csv','w')
hi_csv = open('result2/hi.csv','w')
hr_csv = open('result2/hr.csv','w')
ht_csv = open('result2/ht.csv','w')
hu_csv = open('result2/hu.csv','w')
hy_csv = open('result2/hy.csv','w')
id_csv = open('result2/id.csv','w')
is_csv = open('result2/is.csv','w')
it_csv = open('result2/it.csv','w')
ja_csv = open('result2/ja.csv','w')
jv_csv = open('result2/jv.csv','w')
ka_csv = open('result2/ka.csv','w')
kk_csv = open('result2/kk.csv','w')
km_csv = open('result2/km.csv','w')
kn_csv = open('result2/kn.csv','w')
ko_csv = open('result2/ko.csv','w')
ku_csv = open('result2/ku.csv','w')
ky_csv = open('result2/ky.csv','w')
la_csv = open('result2/la.csv','w')
lb_csv = open('result2/lb.csv','w')
lo_csv = open('result2/lo.csv','w')
lt_csv = open('result2/lt.csv','w')
lv_csv = open('result2/lv.csv','w')
mg_csv = open('result2/mg.csv','w')
mk_csv = open('result2/mk.csv','w')
ml_csv = open('result2/ml.csv','w')
mn_csv = open('result2/mn.csv','w')
mr_csv = open('result2/mr.csv','w')
ms_csv = open('result2/ms.csv','w')
mt_csv = open('result2/mt.csv','w')
nb_csv = open('result2/nb.csv','w')
ne_csv = open('result2/ne.csv','w')
nl_csv = open('result2/nl.csv','w')
nn_csv = open('result2/nn.csv','w')
no_csv = open('result2/no.csv','w')
oc_csv = open('result2/oc.csv','w')
or_csv = open('result2/or.csv','w')
pa_csv = open('result2/pa.csv','w')
pl_csv = open('result2/pl.csv','w')
ps_csv = open('result2/ps.csv','w')
pt_csv = open('result2/pt.csv','w')
qu_csv = open('result2/qu.csv','w')
ro_csv = open('result2/ro.csv','w')
ru_csv = open('result2/ru.csv','w')
rw_csv = open('result2/rw.csv','w')
se_csv = open('result2/se.csv','w')
si_csv = open('result2/si.csv','w')
sk_csv = open('result2/sk.csv','w')
sl_csv = open('result2/sl.csv','w')
sq_csv = open('result2/sq.csv','w')
sr_csv = open('result2/sr.csv','w')
sv_csv = open('result2/sv.csv','w')
sw_csv = open('result2/sw.csv','w')
ta_csv = open('result2/ta.csv','w')
te_csv = open('result2/te.csv','w')
th_csv = open('result2/th.csv','w')
tl_csv = open('result2/tl.csv','w')
tr_csv = open('result2/tr.csv','w')
ug_csv = open('result2/ug.csv','w')
uk_csv = open('result2/uk.csv','w')
ur_csv = open('result2/ur.csv','w')
vi_csv = open('result2/vi.csv','w')
vo_csv = open('result2/vo.csv','w')
wa_csv = open('result2/wa.csv','w')
xh_csv = open('result2/xh.csv','w')
zh_csv = open('result2/zh.csv','w')
zu_csv = open('result2/zu.csv','w')
unknow_csv = open('unknow.csv','w')



### split no-spaces sentence 对长字母句子进行分词 ###
## http://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words
dict_words = open("english.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(dict_words)))) for i,k in enumerate(dict_words))
maxword = max(len(x) for x in dict_words)
def infer_spaces(s):
	"""Uses dynamic programming to infer the location of spaces in a string
	without spaces."""

	# Find the best match for the i first characters, assuming cost has
	# been built for the i-1 first characters.
	# Returns a pair (match_cost, match_length).
	def best_match(i):
		candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
		return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

	# Build the cost array.
	cost = [0]
	for i in range(1,len(s)+1):
		c,k = best_match(i)
		cost.append(c)

	# Backtrack to recover the minimal-cost string.
	out = []
	i = len(s)
	while i>0:
		c,k = best_match(i)
		assert c == cost[i]
		out.append(s[i-k:i])
		i -= k

	return " ".join(reversed(out))


i = 1

###设置需要分析的字段
for caption,tags in reader:

	i = i+1
	word = caption.lower().replace('#',' ').replace('# ',' ').replace('@',' ').replace(',',' ')
	word = re.sub(r'\n',' ',word)
	word = re.sub(r'\r\n',' ',word)
	#.replace('beijing','北京').replace('shanghai','上海').replace('bj','北京').replace('sh','上海').replace('tiananmen','天安门').replace('sanlitun','三里屯')
	words  = ''.join([i for i in word if not i.isdigit()])
	t = str(langid.classify(words))
	l = t[2:4]

	if l!='en' and len(words)>60:
		s = infer_spaces(words)
		d = str(langid.classify(s))
		l = d[2:4]

	if l!='en':
		s = re.sub(r'([a-z])','',words)
		d = d = str(langid.classify(s))
		l = d[2:4]

	if l=='zh' or l=='ja' or l=='ko':
		word_zh = ''.join(re.findall(u"[\u4e00-\u9fa5]+", words))
		word_ko = ''.join(re.findall(u"[\uac00-\ud7ff]+", words))
		word_ja = ''.join(re.findall(u"[\u30a0-\u30ff]+", words))+''.join(re.findall(u"[\u3040-\u309f]+", words))
		word_zh_len = (len(word_zh))/len(words)
		word_ko_len = (len(word_ko))/len(words)
		word_ja_len = (len(word_ja))/len(words)
		word_ja_k = ''.join(re.findall(u"[\u30a0-\u30ff]+", words))
		word_ja_h = ''.join(re.findall(u"[\u3040-\u309f]+", words))

		if len(word_ja_h)>0 or len(word_ja_k)>0:
			l='ja'
		elif word_ko_len>0:
			l='ko'
		else:
			l='zh'

	if l=='zh' and word_ja_len>0:
		langs = 'zh,ja'
	elif l=='zh' and word_ko_len>0 and word_ja_len>0:
		langs = 'zh,ja,ko'
	elif l=='zh' and word_ko_len>0:
		langs = 'zh,ko'
	elif l=='ja' and word_zh_len>0:
		langs = 'ja,zh'
	elif l=='ja' and word_ko_len>0:
		langs = 'ja,ko'
	elif l=='ja' and word_ja_len>0 and word_ko_len>0:
		langs = 'ja,zh,ko'
	elif l=='ko' and word_ja_len>0:
		langs = 'ko,ja'
	elif l=='ko' and word_zh_len>0:
		langs = 'ko,zh'
	elif l=='ko' and word_ja_len>0 and word_zh_len>0:
		langs = 'ko,ja,zh'
	else:
		langs = 'single language'




	if words == 'no caption':
		l ='xx'
	

	
	if l =='xx':
		writer=csv.writer(no_caption_csv, lineterminator='\r\n')
	elif l== 'af':
		writer=csv.writer(af_csv, lineterminator='\r\n')
	elif l== 'am':
		writer=csv.writer(am_csv, lineterminator='\r\n')
	elif l== 'an':
		writer=csv.writer(an_csv, lineterminator='\r\n')
	elif l== 'ar':
		writer=csv.writer(ar_csv, lineterminator='\r\n')
	elif l== 'as':
		writer=csv.writer(as_csv, lineterminator='\r\n')
	elif l== 'az':
		writer=csv.writer(az_csv, lineterminator='\r\n')
	elif l== 'be':
		writer=csv.writer(be_csv, lineterminator='\r\n')
	elif l== 'bg':
		writer=csv.writer(bg_csv, lineterminator='\r\n')
	elif l== 'bn':
		writer=csv.writer(bn_csv, lineterminator='\r\n')
	elif l== 'br':
		writer=csv.writer(br_csv, lineterminator='\r\n')
	elif l== 'bs':
		writer=csv.writer(bs_csv, lineterminator='\r\n')
	elif l== 'ca':
		writer=csv.writer(ca_csv, lineterminator='\r\n')
	elif l== 'cs':
		writer=csv.writer(cs_csv, lineterminator='\r\n')
	elif l== 'cy':
		writer=csv.writer(cy_csv, lineterminator='\r\n')
	elif l== 'da':
		writer=csv.writer(da_csv, lineterminator='\r\n')
	elif l== 'de':
		writer=csv.writer(de_csv, lineterminator='\r\n')
	elif l== 'dz':
		writer=csv.writer(dz_csv, lineterminator='\r\n')
	elif l== 'el':
		writer=csv.writer(el_csv, lineterminator='\r\n')
	elif l== 'en':
		writer=csv.writer(en_csv, lineterminator='\r\n')
	elif l== 'eo':
		writer=csv.writer(eo_csv, lineterminator='\r\n')
	elif l== 'es':
		writer=csv.writer(es_csv, lineterminator='\r\n')
	elif l== 'et':
		writer=csv.writer(et_csv, lineterminator='\r\n')
	elif l== 'eu':
		writer=csv.writer(eu_csv, lineterminator='\r\n')
	elif l== 'fa':
		writer=csv.writer(fa_csv, lineterminator='\r\n')
	elif l== 'fi':
		writer=csv.writer(fi_csv, lineterminator='\r\n')
	elif l== 'fo':
		writer=csv.writer(fo_csv, lineterminator='\r\n')
	elif l== 'fr':
		writer=csv.writer(fr_csv, lineterminator='\r\n')
	elif l== 'ga':
		writer=csv.writer(ga_csv, lineterminator='\r\n')
	elif l== 'gl':
		writer=csv.writer(gl_csv, lineterminator='\r\n')
	elif l== 'gu':
		writer=csv.writer(gu_csv, lineterminator='\r\n')
	elif l== 'he':
		writer=csv.writer(he_csv, lineterminator='\r\n')
	elif l== 'hi':
		writer=csv.writer(hi_csv, lineterminator='\r\n')
	elif l== 'hr':
		writer=csv.writer(hr_csv, lineterminator='\r\n')
	elif l== 'ht':
		writer=csv.writer(ht_csv, lineterminator='\r\n')
	elif l== 'hu':
		writer=csv.writer(hu_csv, lineterminator='\r\n')
	elif l== 'hy':
		writer=csv.writer(hy_csv, lineterminator='\r\n')
	elif l== 'id':
		writer=csv.writer(id_csv, lineterminator='\r\n')
	elif l== 'is':
		writer=csv.writer(is_csv, lineterminator='\r\n')
	elif l== 'it':
		writer=csv.writer(it_csv, lineterminator='\r\n')
	elif l== 'ja':
		writer=csv.writer(ja_csv, lineterminator='\r\n')
	elif l== 'jv':
		writer=csv.writer(jv_csv, lineterminator='\r\n')
	elif l== 'ka':
		writer=csv.writer(ka_csv, lineterminator='\r\n')
	elif l== 'kk':
		writer=csv.writer(kk_csv, lineterminator='\r\n')
	elif l== 'km':
		writer=csv.writer(km_csv, lineterminator='\r\n')
	elif l== 'kn':
		writer=csv.writer(kn_csv, lineterminator='\r\n')
	elif l== 'ko':
		writer=csv.writer(ko_csv, lineterminator='\r\n')
	elif l== 'ku':
		writer=csv.writer(ku_csv, lineterminator='\r\n')
	elif l== 'ky':
		writer=csv.writer(ky_csv, lineterminator='\r\n')
	elif l== 'la':
		writer=csv.writer(la_csv, lineterminator='\r\n')
	elif l== 'lb':
		writer=csv.writer(lb_csv, lineterminator='\r\n')
	elif l== 'lo':
		writer=csv.writer(lo_csv, lineterminator='\r\n')
	elif l== 'lt':
		writer=csv.writer(lt_csv, lineterminator='\r\n')
	elif l== 'lv':
		writer=csv.writer(lv_csv, lineterminator='\r\n')
	elif l== 'mg':
		writer=csv.writer(mg_csv, lineterminator='\r\n')
	elif l== 'mk':
		writer=csv.writer(mk_csv, lineterminator='\r\n')
	elif l== 'ml':
		writer=csv.writer(ml_csv, lineterminator='\r\n')
	elif l== 'mn':
		writer=csv.writer(mn_csv, lineterminator='\r\n')
	elif l== 'mr':
		writer=csv.writer(mr_csv, lineterminator='\r\n')
	elif l== 'ms':
		writer=csv.writer(ms_csv, lineterminator='\r\n')
	elif l== 'mt':
		writer=csv.writer(mt_csv, lineterminator='\r\n')
	elif l== 'nb':
		writer=csv.writer(nb_csv, lineterminator='\r\n')
	elif l== 'ne':
		writer=csv.writer(ne_csv, lineterminator='\r\n')
	elif l== 'nl':
		writer=csv.writer(nl_csv, lineterminator='\r\n')
	elif l== 'nn':
		writer=csv.writer(nn_csv, lineterminator='\r\n')
	elif l== 'no':
		writer=csv.writer(no_csv, lineterminator='\r\n')
	elif l== 'oc':
		writer=csv.writer(oc_csv, lineterminator='\r\n')
	elif l== 'or':
		writer=csv.writer(or_csv, lineterminator='\r\n')
	elif l== 'pa':
		writer=csv.writer(pa_csv, lineterminator='\r\n')
	elif l== 'pl':
		writer=csv.writer(pl_csv, lineterminator='\r\n')
	elif l== 'ps':
		writer=csv.writer(ps_csv, lineterminator='\r\n')
	elif l== 'pt':
		writer=csv.writer(pt_csv, lineterminator='\r\n')
	elif l== 'qu':
		writer=csv.writer(qu_csv, lineterminator='\r\n')
	elif l== 'ro':
		writer=csv.writer(ro_csv, lineterminator='\r\n')
	elif l== 'ru':
		writer=csv.writer(ru_csv, lineterminator='\r\n')
	elif l== 'rw':
		writer=csv.writer(rw_csv, lineterminator='\r\n')
	elif l== 'se':
		writer=csv.writer(se_csv, lineterminator='\r\n')
	elif l== 'si':
		writer=csv.writer(si_csv, lineterminator='\r\n')
	elif l== 'sk':
		writer=csv.writer(sk_csv, lineterminator='\r\n')
	elif l== 'sl':
		writer=csv.writer(sl_csv, lineterminator='\r\n')
	elif l== 'sq':
		writer=csv.writer(sq_csv, lineterminator='\r\n')
	elif l== 'sr':
		writer=csv.writer(sr_csv, lineterminator='\r\n')
	elif l== 'sv':
		writer=csv.writer(sv_csv, lineterminator='\r\n')
	elif l== 'sw':
		writer=csv.writer(sw_csv, lineterminator='\r\n')
	elif l== 'ta':
		writer=csv.writer(ta_csv, lineterminator='\r\n')
	elif l== 'te':
		writer=csv.writer(te_csv, lineterminator='\r\n')
	elif l== 'th':
		writer=csv.writer(th_csv, lineterminator='\r\n')
	elif l== 'tl':
		writer=csv.writer(tl_csv, lineterminator='\r\n')
	elif l== 'tr':
		writer=csv.writer(tr_csv, lineterminator='\r\n')
	elif l== 'ug':
		writer=csv.writer(ug_csv, lineterminator='\r\n')
	elif l== 'uk':
		writer=csv.writer(uk_csv, lineterminator='\r\n')
	elif l== 'ur':
		writer=csv.writer(ur_csv, lineterminator='\r\n')
	elif l== 'vi':
		writer=csv.writer(vi_csv, lineterminator='\r\n')
	elif l== 'vo':
		writer=csv.writer(vo_csv, lineterminator='\r\n')
	elif l== 'wa':
		writer=csv.writer(wa_csv, lineterminator='\r\n')
	elif l== 'xh':
		writer=csv.writer(xh_csv, lineterminator='\r\n')
	elif l== 'zh':
		writer=csv.writer(zh_csv, lineterminator='\r\n')
	elif l== 'zu':
		writer=csv.writer(zu_csv, lineterminator='\r\n')
	else:
		writer=csv.writer(unknow_csv, lineterminator='\r\n')


	
	print (i)



	
	writer.writerow([id_hash,time,lat,lng,link,filter,username,words,l,langs])



# from guess_language import guess_language
# f = open("sample.txt")
# lines = list(f)
# f.close()
# f1 = open('result.txt','w')
# for eachline in lines:
# 	l = guess_language(eachline)
# 	f1.write(l)
# 	f1.write('\n')
# 	print (l)

# for n in re.findall(ur'[\u0021-\u007a]+',lines):
# 		f1.write(n.encode('utf8'))
# 		f1.write('\n')
# 		print n










	#print eachline
#sample = u'한국어'
# for n in re.findall(ur'[\ue757-\ue757]+',words):
# 	f1.write(n.encode('utf8'))
# 	f1.write('\n')
# 	print n
	

# 
# for n in re.findall(ur'[\u4e00-\u9fff]+',sample):
#     print n