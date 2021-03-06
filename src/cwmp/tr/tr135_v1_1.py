#!/usr/bin/python
# Copyright 2011 Google Inc. All Rights Reserved.
#
# AUTO-GENERATED BY parse-schema.py
#
# DO NOT EDIT!!
#
#pylint: disable-msg=C6202
#pylint: disable-msg=C6409
#pylint: disable-msg=C6310
# These should not actually be necessary (bugs in gpylint?):
#pylint: disable-msg=E1101
#pylint: disable-msg=W0231
#
"""Auto-generated from spec: urn:broadband-forum-org:tr-135-1-1."""

import core
from tr135_v1_0 import STBService_v1_0


class STBService_v1_1(STBService_v1_0):
  """Represents STBService_v1_1."""

  def __init__(self, **defaults):
    STBService_v1_0.__init__(self, defaults=defaults)
    self.Export(lists=['STBService'])

  class STBService(STBService_v1_0.STBService):
    """Represents STBService_v1_1.STBService.{i}."""

    def __init__(self, **defaults):
      STBService_v1_0.STBService.__init__(self, defaults=defaults)
      self.Export(objects=['AVPlayers',
                           'AVStreams',
                           'Applications',
                           'Capabilities',
                           'Components',
                           'ServiceMonitoring'])

    class AVPlayers(STBService_v1_0.STBService.AVPlayers):
      """Represents STBService_v1_1.STBService.{i}.AVPlayers."""

      def __init__(self, **defaults):
        STBService_v1_0.STBService.AVPlayers.__init__(self, defaults=defaults)
        self.Export(params=['PreferredBehaviour',
                            'ResetPINCode'],
                    lists=['AVPlayer'])

      class AVPlayer(STBService_v1_0.STBService.AVPlayers.AVPlayer):
        """Represents STBService_v1_1.STBService.{i}.AVPlayers.AVPlayer.{i}."""
        pass

    class AVStreams(STBService_v1_0.STBService.AVStreams):
      """Represents STBService_v1_1.STBService.{i}.AVStreams."""

      def __init__(self, **defaults):
        STBService_v1_0.STBService.AVStreams.__init__(self, defaults=defaults)
        self.Export(lists=['AVStream'])

      class AVStream(STBService_v1_0.STBService.AVStreams.AVStream):
        """Represents STBService_v1_1.STBService.{i}.AVStreams.AVStream.{i}."""
        pass

    class Applications(STBService_v1_0.STBService.Applications):
      """Represents STBService_v1_1.STBService.{i}.Applications."""

      def __init__(self, **defaults):
        STBService_v1_0.STBService.Applications.__init__(self, defaults=defaults)
        self.Export(params=['ServiceProviderNumberOfEntries'],
                    objects=['CDSPull',
                             'CDSPush'],
                    lists=['ServiceProvider'])

      class CDSPull(core.Exporter):
        """Represents STBService_v1_1.STBService.{i}.Applications.CDSPull."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['ContentItemNumberOfEntries',
                              'Reference'],
                      lists=['ContentItem'])

        class ContentItem(core.Exporter):
          """Represents STBService_v1_1.STBService.{i}.Applications.CDSPull.ContentItem.{i}."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['ContentReferenceId',
                                'DeleteItem',
                                'VersionNumber'])

      class CDSPush(core.Exporter):
        """Represents STBService_v1_1.STBService.{i}.Applications.CDSPush."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['ContentItemNumberOfEntries',
                              'Reference'],
                      lists=['ContentItem'])

        class ContentItem(core.Exporter):
          """Represents STBService_v1_1.STBService.{i}.Applications.CDSPush.ContentItem.{i}."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['ContentReferenceId',
                                'DeleteItem',
                                'VersionNumber'])

      class ServiceProvider(core.Exporter):
        """Represents STBService_v1_1.STBService.{i}.Applications.ServiceProvider.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['ActiveBCGServers',
                              'Domain',
                              'Name',
                              'ServiceDiscoveryServer'])

    class Capabilities(STBService_v1_0.STBService.Capabilities):
      """Represents STBService_v1_1.STBService.{i}.Capabilities."""

      def __init__(self, **defaults):
        STBService_v1_0.STBService.Capabilities.__init__(self, defaults=defaults)
        self.Export(objects=['CDS',
                             'HDMI',
                             'PVR',
                             'ServiceMonitoring',
                             'VideoOutput'])

      class CDS(core.Exporter):
        """Represents STBService_v1_1.STBService.{i}.Capabilities.CDS."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['PullCapable',
                              'PushCapable'])

      class HDMI(core.Exporter):
        """Represents STBService_v1_1.STBService.{i}.Capabilities.HDMI."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['CECSupport',
                              'HDMI3D',
                              'SupportedResolutions'])

      class PVR(STBService_v1_0.STBService.Capabilities.PVR):
        """Represents STBService_v1_1.STBService.{i}.Capabilities.PVR."""

        def __init__(self, **defaults):
          STBService_v1_0.STBService.Capabilities.PVR.__init__(self, defaults=defaults)
          self.Export(params=['MaxIOStreams'])

      class ServiceMonitoring(STBService_v1_0.STBService.Capabilities.ServiceMonitoring):
        """Represents STBService_v1_1.STBService.{i}.Capabilities.ServiceMonitoring."""

        def __init__(self, **defaults):
          STBService_v1_0.STBService.Capabilities.ServiceMonitoring.__init__(self, defaults=defaults)
          self.Export(params=['HighLevelMetricNames',
                              'MaxEventsPerSampleInterval',
                              'ServiceTypes'])

      class VideoOutput(STBService_v1_0.STBService.Capabilities.VideoOutput):
        """Represents STBService_v1_1.STBService.{i}.Capabilities.VideoOutput."""

        def __init__(self, **defaults):
          STBService_v1_0.STBService.Capabilities.VideoOutput.__init__(self, defaults=defaults)
          self.Export(params=['DisplayFormats'])

    class Components(STBService_v1_0.STBService.Components):
      """Represents STBService_v1_1.STBService.{i}.Components."""

      def __init__(self, **defaults):
        STBService_v1_0.STBService.Components.__init__(self, defaults=defaults)
        self.Export(params=['AudioDecoderNumberOfEntries',
                            'AudioOutputNumberOfEntries',
                            'CANumberOfEntries',
                            'DRMNumberOfEntries',
                            'FrontEndNumberOfEntries',
                            'HDMINumberOfEntries',
                            'SCARTNumberOfEntries',
                            'SPDIFNumberOfEntries',
                            'VideoDecoderNumberOfEntries',
                            'VideoOutputNumberOfEntries'],
                    objects=['PVR'],
                    lists=['AudioDecoder',
                           'AudioOutput',
                           'FrontEnd',
                           'HDMI',
                           'SCART',
                           'SPDIF',
                           'VideoDecoder',
                           'VideoOutput'])

      class AudioDecoder(STBService_v1_0.STBService.Components.AudioDecoder):
        """Represents STBService_v1_1.STBService.{i}.Components.AudioDecoder.{i}."""
        pass

      class AudioOutput(STBService_v1_0.STBService.Components.AudioOutput):
        """Represents STBService_v1_1.STBService.{i}.Components.AudioOutput.{i}."""
        pass

      class FrontEnd(STBService_v1_0.STBService.Components.FrontEnd):
        """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}."""

        def __init__(self, **defaults):
          STBService_v1_0.STBService.Components.FrontEnd.__init__(self, defaults=defaults)
          self.Export(objects=['DVBT',
                               'IP'])

        class DVBT(STBService_v1_0.STBService.Components.FrontEnd.DVBT):
          """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.DVBT."""

          def __init__(self, **defaults):
            STBService_v1_0.STBService.Components.FrontEnd.DVBT.__init__(self, defaults=defaults)
            self.Export(objects=['Modulation',
                                 'Service',
                                 'ServiceListDatabase'])

          class Modulation(STBService_v1_0.STBService.Components.FrontEnd.DVBT.Modulation):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.DVBT.Modulation."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.Components.FrontEnd.DVBT.Modulation.__init__(self, defaults=defaults)
              self.Export(params=['HierarchicalInformation'])

          class Service(core.Exporter):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.DVBT.Service."""

            def __init__(self, **defaults):
              core.Exporter.__init__(self, defaults=defaults)
              self.Export(params=['CurrentLogicalChannel',
                                  'CurrentService'])

          class ServiceListDatabase(STBService_v1_0.STBService.Components.FrontEnd.DVBT.ServiceListDatabase):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.DVBT.ServiceListDatabase."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.__init__(self, defaults=defaults)
              self.Export(lists=['LogicalChannel'])

            class LogicalChannel(STBService_v1_0.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.LogicalChannel):
              """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.DVBT.ServiceListDatabase.LogicalChannel.{i}."""

              def __init__(self, **defaults):
                STBService_v1_0.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.LogicalChannel.__init__(self, defaults=defaults)
                self.Export(lists=['Service'])

              class Service(STBService_v1_0.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.LogicalChannel.Service):
                """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.DVBT.ServiceListDatabase.LogicalChannel.{i}.Service.{i}."""

                def __init__(self, **defaults):
                  STBService_v1_0.STBService.Components.FrontEnd.DVBT.ServiceListDatabase.LogicalChannel.Service.__init__(self, defaults=defaults)
                  self.Export(params=['CBER',
                                      'Name',
                                      'SNR'])

        class IP(STBService_v1_0.STBService.Components.FrontEnd.IP):
          """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP."""

          def __init__(self, **defaults):
            STBService_v1_0.STBService.Components.FrontEnd.IP.__init__(self, defaults=defaults)
            self.Export(objects=['FEC',
                                 'ForceMonitor',
                                 'IGMP',
                                 'RTPAVPF'],
                        lists=['Inbound',
                               'Outbound'])

          class FEC(core.Exporter):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP.FEC."""

            def __init__(self, **defaults):
              core.Exporter.__init__(self, defaults=defaults)
              self.Export(params=['ECOperationStatus',
                                  'Enable',
                                  'OperationMode'])

          class ForceMonitor(core.Exporter):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP.ForceMonitor."""

            def __init__(self, **defaults):
              core.Exporter.__init__(self, defaults=defaults)
              self.Export(params=['Enable',
                                  'Status',
                                  'URI'])

          class IGMP(STBService_v1_0.STBService.Components.FrontEnd.IP.IGMP):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP.IGMP."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.Components.FrontEnd.IP.IGMP.__init__(self, defaults=defaults)
              self.Export(lists=['ClientGroup',
                                 'ClientGroupStats'])

            class ClientGroup(STBService_v1_0.STBService.Components.FrontEnd.IP.IGMP.ClientGroup):
              """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP.IGMP.ClientGroup.{i}."""
              pass

            class ClientGroupStats(STBService_v1_0.STBService.Components.FrontEnd.IP.IGMP.ClientGroupStats):
              """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP.IGMP.ClientGroupStats.{i}."""
              pass

          class Inbound(STBService_v1_0.STBService.Components.FrontEnd.IP.Inbound):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP.Inbound.{i}."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.Components.FrontEnd.IP.Inbound.__init__(self, defaults=defaults)
              self.Export(params=['Name'])

          class Outbound(STBService_v1_0.STBService.Components.FrontEnd.IP.Outbound):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP.Outbound.{i}."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.Components.FrontEnd.IP.Outbound.__init__(self, defaults=defaults)
              self.Export(params=['Name'])

          class RTPAVPF(STBService_v1_0.STBService.Components.FrontEnd.IP.RTPAVPF):
            """Represents STBService_v1_1.STBService.{i}.Components.FrontEnd.{i}.IP.RTPAVPF."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.Components.FrontEnd.IP.RTPAVPF.__init__(self, defaults=defaults)
              self.Export(params=['ECOperationStatus',
                                  'Enable',
                                  'OperationMode'])

      class HDMI(core.Exporter):
        """Represents STBService_v1_1.STBService.{i}.Components.HDMI.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['Enable',
                              'Name',
                              'ResolutionMode',
                              'ResolutionValue',
                              'Status'],
                      objects=['DisplayDevice'])

        class DisplayDevice(core.Exporter):
          """Represents STBService_v1_1.STBService.{i}.Components.HDMI.{i}.DisplayDevice."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['AutoLipSyncSupport',
                                'CECSupport',
                                'EEDID',
                                'HDMI3DPresent',
                                'Name',
                                'PreferredResolution',
                                'Status',
                                'SupportedResolutions',
                                'VideoLatency'])

      class PVR(STBService_v1_0.STBService.Components.PVR):
        """Represents STBService_v1_1.STBService.{i}.Components.PVR."""

        def __init__(self, **defaults):
          STBService_v1_0.STBService.Components.PVR.__init__(self, defaults=defaults)
          self.Export(lists=['Storage'])

        class Storage(STBService_v1_0.STBService.Components.PVR.Storage):
          """Represents STBService_v1_1.STBService.{i}.Components.PVR.Storage.{i}."""

          def __init__(self, **defaults):
            STBService_v1_0.STBService.Components.PVR.Storage.__init__(self, defaults=defaults)
            self.Export(params=['Name'])

      class SCART(STBService_v1_0.STBService.Components.SCART):
        """Represents STBService_v1_1.STBService.{i}.Components.SCART.{i}."""
        pass

      class SPDIF(core.Exporter):
        """Represents STBService_v1_1.STBService.{i}.Components.SPDIF.{i}."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(params=['AudioDelay',
                              'Enable',
                              'ForcePCM',
                              'Name',
                              'Passthrough',
                              'Status'])

      class VideoDecoder(STBService_v1_0.STBService.Components.VideoDecoder):
        """Represents STBService_v1_1.STBService.{i}.Components.VideoDecoder.{i}."""
        pass

      class VideoOutput(STBService_v1_0.STBService.Components.VideoOutput):
        """Represents STBService_v1_1.STBService.{i}.Components.VideoOutput.{i}."""

        def __init__(self, **defaults):
          STBService_v1_0.STBService.Components.VideoOutput.__init__(self, defaults=defaults)
          self.Export(params=['AspectRatioBehaviour',
                              'ColorbarEnable',
                              'DisplayFormat',
                              'Status'])

    class ServiceMonitoring(STBService_v1_0.STBService.ServiceMonitoring):
      """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring."""

      def __init__(self, **defaults):
        STBService_v1_0.STBService.ServiceMonitoring.__init__(self, defaults=defaults)
        self.Export(params=['EventsPerSampleInterval',
                            'ForceSample',
                            'ReportSamples'],
                    objects=['GlobalOperation'],
                    lists=['MainStream'])

      class GlobalOperation(core.Exporter):
        """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.GlobalOperation."""

        def __init__(self, **defaults):
          core.Exporter.__init__(self, defaults=defaults)
          self.Export(objects=['Sample',
                               'Total'])

        class Sample(core.Exporter):
          """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.GlobalOperation.Sample."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['MaximumPortalResponse',
                                'MinimumPortalResponse',
                                'PortalResponse'])

        class Total(core.Exporter):
          """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.GlobalOperation.Total."""

          def __init__(self, **defaults):
            core.Exporter.__init__(self, defaults=defaults)
            self.Export(params=['MaximumPortalResponse',
                                'MinimumPortalResponse',
                                'ServiceAccessTime'])

      class MainStream(STBService_v1_0.STBService.ServiceMonitoring.MainStream):
        """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}."""

        def __init__(self, **defaults):
          STBService_v1_0.STBService.ServiceMonitoring.MainStream.__init__(self, defaults=defaults)
          self.Export(params=['ChannelChangeFailureTimeout'],
                      objects=['Sample',
                               'Total'])

        class Sample(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample):
          """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Sample."""

          def __init__(self, **defaults):
            STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.__init__(self, defaults=defaults)
            self.Export(params=['SampleSeconds'],
                        objects=['DejitteringStats',
                                 'TCPStats',
                                 'VideoDecoderStats',
                                 'VideoResponseStats'],
                        lists=['HighLevelMetricStats'])

          class DejitteringStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.DejitteringStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Sample.DejitteringStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.DejitteringStats.__init__(self, defaults=defaults)
              self.Export(params=['EmptyBufferTime'])

          class HighLevelMetricStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.HighLevelMetricStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Sample.HighLevelMetricStats.{i}."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.HighLevelMetricStats.__init__(self, defaults=defaults)
              self.Export(params=['Enable',
                                  'Metric',
                                  'Metric1',
                                  'Metric1Failures',
                                  'Metric1Threshold',
                                  'Metric2',
                                  'Metric2Failures',
                                  'Metric2Threshold',
                                  'MetricFailures',
                                  'MetricSampleInterval',
                                  'MetricThreshold',
                                  'Status'])

          class TCPStats(core.Exporter):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Sample.TCPStats."""

            def __init__(self, **defaults):
              core.Exporter.__init__(self, defaults=defaults)
              self.Export(params=['BytesReceived',
                                  'PacketsReceived',
                                  'PacketsRetransmitted',
                                  'SampleSeconds'])

          class VideoDecoderStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.VideoDecoderStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Sample.VideoDecoderStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.VideoDecoderStats.__init__(self, defaults=defaults)
              self.Export(params=['FrameRate'])

          class VideoResponseStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.VideoResponseStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Sample.VideoResponseStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Sample.VideoResponseStats.__init__(self, defaults=defaults)
              self.Export(params=['AccessSuccesses',
                                  'AverageVoDControlResponse',
                                  'ChannelChangeFailures',
                                  'CompletionCount',
                                  'MaximumVoDControlResponse',
                                  'MinimumVoDControlResponse',
                                  'RequestedTransactions',
                                  'VideoSystemResponse',
                                  'VoDControlResponse'])

        class Total(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total):
          """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Total."""

          def __init__(self, **defaults):
            STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.__init__(self, defaults=defaults)
            self.Export(params=['TotalSeconds'],
                        objects=['AudioDecoderStats',
                                 'DejitteringStats',
                                 'MPEG2TSStats',
                                 'RTPStats',
                                 'TCPStats',
                                 'VideoDecoderStats',
                                 'VideoResponseStats'])

          class AudioDecoderStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.AudioDecoderStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Total.AudioDecoderStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.AudioDecoderStats.__init__(self, defaults=defaults)
              self.Export(params=['TotalSeconds'])

          class DejitteringStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.DejitteringStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Total.DejitteringStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.DejitteringStats.__init__(self, defaults=defaults)
              self.Export(params=['EmptyBufferTime',
                                  'TotalSeconds'])

          class MPEG2TSStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.MPEG2TSStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Total.MPEG2TSStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.MPEG2TSStats.__init__(self, defaults=defaults)
              self.Export(params=['TotalSeconds'])

          class RTPStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.RTPStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Total.RTPStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.RTPStats.__init__(self, defaults=defaults)
              self.Export(params=['TotalSeconds'])

          class TCPStats(core.Exporter):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Total.TCPStats."""

            def __init__(self, **defaults):
              core.Exporter.__init__(self, defaults=defaults)
              self.Export(params=['BytesReceived',
                                  'PacketsReceived',
                                  'PacketsRetransmitted',
                                  'TotalSeconds'])

          class VideoDecoderStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.VideoDecoderStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Total.VideoDecoderStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.VideoDecoderStats.__init__(self, defaults=defaults)
              self.Export(params=['FrameRate',
                                  'TotalSeconds'])

          class VideoResponseStats(STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.VideoResponseStats):
            """Represents STBService_v1_1.STBService.{i}.ServiceMonitoring.MainStream.{i}.Total.VideoResponseStats."""

            def __init__(self, **defaults):
              STBService_v1_0.STBService.ServiceMonitoring.MainStream.Total.VideoResponseStats.__init__(self, defaults=defaults)
              self.Export(params=['AccessSuccesses',
                                  'ChannelChangeFailures',
                                  'ChannelFailures',
                                  'CompletionCount',
                                  'MaximumVoDControlResponse',
                                  'MinimumVoDControlResponse',
                                  'RequestedTransactions',
                                  'TotalSeconds'])


if __name__ == '__main__':
  print core.DumpSchema(STBService_v1_1)
