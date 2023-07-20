# A quick python file to print a table of CPU times for solved instances
from itertools import product
from pandas import read_csv
from pathlib import Path
from sys import stdout

def main() -> None:
    results_dir = Path(__file__).parent

    wanted_instrumentors = list(map('-'.join, product(
        ('bb', 'cc'),
        ('gams', 'lemon'),
    )))

    wanted_apps = ['tcas','schedule2','schedule','replace','tot_info', 'print_tokens2']
    
    df = read_csv(results_dir / 'compile-results.csv')
    df = df[df['application'].isin(wanted_apps)]
    df = df[df['instrumentor'].isin(wanted_instrumentors)]
    df = df[df['success']==True]
    df=df.drop(columns=['version','trial','memoryuse','success','failurereason'])
#    print(df)
    grouped = df.groupby(['application','instrumentor'])
    df2=grouped.mean()
#    print(df2)
    
    print_compile_time_table(df2)
        
          
#    pivoted = df.pivot_table(index='application',
#                             columns='instrumentor',
#                             values='compiletime',
#                             aggfunc = [numpy.mean])
#    print(pivoted)

# Super kludgy, should have been able to do this more nicely

def print_compile_time_table(df):
    print("Application, Instrumentation, gams, lemon, speedup")

    tcas_bbgams = df.loc[('tcas', 'bb-gams'),'compiletime']
    tcas_bblemon = df.loc[('tcas', 'bb-lemon'),'compiletime']
    print("tcas,basic blocks," + str(tcas_bbgams) + "," + str(tcas_bblemon) + "," + str(tcas_bbgams/tcas_bblemon))

    schedule2_bbgams = df.loc[('schedule2', 'bb-gams'),'compiletime']
    schedule2_bblemon = df.loc[('schedule2', 'bb-lemon'),'compiletime']
    print("schedule2,basic blocks," + str(schedule2_bbgams) + "," + str(schedule2_bblemon) + "," + str(schedule2_bbgams/schedule2_bblemon))

    tcas_ccgams = df.loc[('tcas', 'cc-gams'),'compiletime']
    tcas_cclemon = df.loc[('tcas', 'cc-lemon'),'compiletime']
    print("tcas,call sites," + str(tcas_ccgams) + "," + str(tcas_cclemon) + "," + str(tcas_ccgams/tcas_cclemon))

    schedule2_ccgams = df.loc[('schedule2', 'cc-gams'),'compiletime']
    schedule2_cclemon = df.loc[('schedule2', 'cc-lemon'),'compiletime']
    print("schedule2,call sites," + str(schedule2_ccgams) + "," + str(schedule2_cclemon) + "," + str(schedule2_ccgams/schedule2_cclemon))

    schedule_ccgams = df.loc[('schedule', 'cc-gams'),'compiletime']
    schedule_cclemon = df.loc[('schedule', 'cc-lemon'),'compiletime']
    print("schedule,call sites," + str(schedule_ccgams) + "," + str(schedule_cclemon) + "," + str(schedule_ccgams/schedule_cclemon))

    replace_ccgams = df.loc[('replace', 'cc-gams'),'compiletime']
    replace_cclemon = df.loc[('replace', 'cc-lemon'),'compiletime']
    print("replace,call sites," + str(replace_ccgams) + "," + str(replace_cclemon) + "," + str(replace_ccgams/replace_cclemon))

    tot_info_ccgams = df.loc[('tot_info', 'cc-gams'),'compiletime']
    tot_info_cclemon = df.loc[('tot_info', 'cc-lemon'),'compiletime']
    print("tot_info,call sites," + str(tot_info_ccgams) + "," + str(tot_info_cclemon) + "," + str(tot_info_ccgams/tot_info_cclemon))

    print_tokens2_ccgams = df.loc[('print_tokens2', 'cc-gams'),'compiletime']
    print_tokens2_cclemon = df.loc[('print_tokens2', 'cc-lemon'),'compiletime']
    print("print_tokens2,call sites," + str(print_tokens2_ccgams) + "," + str(print_tokens2_cclemon) + "," + str(print_tokens2_ccgams/print_tokens2_cclemon))
    


if __name__ == '__main__':
    main()
