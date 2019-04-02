module tf.graph.scene {
  import RenderNodeInfo = tf.graph.render.RenderNodeInfo;
  type Selection = d3.Selection<any, any, any, any>;

  // This technically extends Polymer.Component whose constructor is not
  // accessible.
  export abstract class TfGraphScene extends HTMLElement {
    maxMetanodeLabelLength: number;
    maxMetanodeLabelLengthLargeFont: number;
    maxMetanodeLabelLengthFontSize: number;
    templateIndex: () => {};
    colorBy: string;

    abstract fire(eventName: string, daat: any): void;
    abstract addNodeGroup(name: string, selection: Selection): void;
    abstract removeNodeGroup(name: string): void;
    abstract removeAnnotationGroup(name: string): void;
    abstract isNodeExpanded(node: RenderNodeInfo): boolean;
    abstract isNodeHighlighted(nodeName: string): boolean;
    abstract isNodeSelected(nodeName: string): boolean;
    abstract getAnnotationGroupsIndex(name: string): Selection;
    abstract getGraphSvgRoot(): SVGElement;
  }
}
