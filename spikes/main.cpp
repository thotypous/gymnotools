#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>
#include <limits>

#include <QStringList>
#include <QtDebug>

#include "common/commoninit.h"
#include "common/defaultparams.h"
#include "common/sigcfg.h"
#include "common/signalfile.h"
#include "common/excludedintervals.h"

static void spikeDiscriminator(SignalFile &sigfile, QFile &outfile, bool fixedwin,
                               float detection, float minlevel,
                               float minratio, int stopsamples,
                               float saturationLow, float saturationHigh,
                               ExcludedIntervalList &intervals)
{
    SignalBuffer buf(2*EODSamples);
}

static int usage(const char *progname)
{
    fprintf(stderr, "%s [options] input.I32 output.spikes\n",
            progname);
    fprintf(stderr, "options:\n"
            "  -f|--fixedwin       Fixed window (use for single-fish data files)\n"
            "  -n|--numtaps=n      Number of taps (lowpass filter)\n"
            "  -c|--cutoff=c       Cutoff frequency (lowpass filter)\n"
            "  -d|--detection=d    Threshold for detecting a spike\n"
            "  -l|--minlevel=l     Minimum level to stop detection\n"
            "  -r|--minratio=r     Ratio of the maximum level to stop detection\n"
            "  -s|--stopsamples=s  Samples below level to stop detection\n"
            "  -e|--exclude=file   File containing intervals/channels to exclude\n"
            "  -z|--saturation=a,b Low and high saturation levels to filter out\n");
    return 1;
}

int main(int argc, char **argv)
{
    commonInit();

    bool fixedwin = false;
    int numtaps = defaultLowpassNumTaps;
    float cutoff = defaultLowPassCutoff;
    float detection = defaultDetectionThreshold;
    float minlevel = defaultMinLevel;
    float minratio = defaultMinRatio;
    int stopsamples = defaultStopSamples;
    float saturationLow = -std::numeric_limits<float>::infinity();
    float saturationHigh = std::numeric_limits<float>::infinity();
    ExcludedIntervalList intervals;

    while(1) {
        int option_index = 0;
        static struct option long_options[] = {
            { "fixedwin",    no_argument,       0, 'f' },
            { "numtaps",     required_argument, 0, 'n' },
            { "cutoff",      required_argument, 0, 'c' },
            { "detection",   required_argument, 0, 'd' },
            { "minlevel",    required_argument, 0, 'l' },
            { "minratio",    required_argument, 0, 'r' },
            { "stopsamples", required_argument, 0, 's' },
            { "exclude",     required_argument, 0, 'e' },
            { "saturation",  required_argument, 0, 'z' },
            { 0, 0, 0, 0 }
        };

        int c = getopt_long(argc, argv, "fn:c:d:l:r:s:e:z:",
                            long_options, &option_index);
        if(c == -1)
            break;

        switch(c) {
        case 'f':
            fixedwin = true;
            break;
        case 'n':
            numtaps = QString(optarg).toInt();
            break;
        case 'c':
            cutoff = QString(optarg).toFloat();
            break;
        case 'd':
            detection = QString(optarg).toFloat();
            break;
        case 'l':
            minlevel = QString(optarg).toFloat();
            break;
        case 'r':
            minratio = QString(optarg).toFloat();
            break;
        case 's':
            stopsamples = QString(optarg).toInt();
            break;
        case 'e':
            {
                QFile file(optarg);
                if(!file.open(QIODevice::ReadOnly)) {
                    fprintf(stderr, "Can't open exclude file (%s).\n", optarg);
                    return 1;
                }
                intervals.parseFile(file);
            }
            break;
        case 'z':
            if(!strcmp(optarg, "def")) {
                saturationLow = defaultSaturationLow;
                saturationHigh = defaultSaturationHigh;
            }
            else {
                QStringList sl = QString(optarg).split(",");
                if(sl.count() != 2) {
                    fprintf(stderr, "--saturation argument must be 'def' or"
                            " a list of two numbers\n");
                    return 1;
                }
                saturationLow = sl.at(0).toFloat();
                saturationHigh = sl.at(1).toFloat();
            }
            break;
        default:
            return usage(argv[0]);
        }
    }

    if(argc - optind != 2)
        return usage(argv[0]);

    const char *inFilename = argv[optind];
    SignalFile sigfile(inFilename);
    sigfile.setFilter(numtaps, cutoff);

    if(!sigfile.open(QIODevice::ReadOnly)) {
        fprintf(stderr, "Can't open input file (%s).\n", inFilename);
        return 1;
    }

    const char *outFilename = argv[optind+1];
    QFile outfile(outFilename);

    if(!outfile.open(QIODevice::WriteOnly)) {
        fprintf(stderr, "Can't open output file (%s).\n", outFilename);
        return 1;
    }

    spikeDiscriminator(sigfile, outfile, fixedwin, detection,
                       minlevel, minratio, stopsamples,
                       saturationLow, saturationHigh, intervals);

    return 0;
}
