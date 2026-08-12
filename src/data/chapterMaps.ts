// ---------------------------------------------------------------------------
// Argument map layouts, one per chapter.
// Nodes: id -> [x, y, layer]. Edges: [from, to, label].
// Copy strings are provided per language by each chapter page.
// ---------------------------------------------------------------------------

export interface MapLayout {
  nodes: Record<string, [number, number, 1 | 2 | 3]>;
  edges: Array<[string, string, string]>;
}

export const POE_MAP: MapLayout = {
  nodes: {
    'POE-001': [70, 70, 1],
    'POE-002': [190, 70, 1],
    'POE-003': [310, 70, 1],
    'POE-004': [430, 70, 1],
    'POE-005': [550, 70, 1],
    'POE-006': [670, 70, 1],
    'POE-007': [70, 220, 2],
    'POE-008': [190, 220, 2],
    'POE-009': [310, 220, 2],
    'POE-010': [430, 220, 2],
    'POE-011': [550, 220, 2],
    'POE-012': [670, 220, 2],
    'POE-013': [240, 370, 3],
    'POE-014': [420, 370, 3],
    'POE-015': [600, 370, 3],
  },
  edges: [
    ['POE-001', 'POE-007', 'feeds'],
    ['POE-005', 'POE-007', 'feeds'],
    ['POE-006', 'POE-007', 'feeds'],
    ['POE-006', 'POE-008', 'modally'],
    ['POE-005', 'POE-008', 'feeds'],
    ['POE-007', 'POE-008', 'responds to'],
    ['POE-007', 'POE-009', 'extends'],
    ['POE-009', 'POE-010', 'specifies'],
    ['POE-008', 'POE-011', 'extends'],
    ['POE-011', 'POE-012', 'is targeted by'],
    ['POE-009', 'POE-013', 'is met by'],
    ['POE-010', 'POE-013', 'is met by'],
    ['POE-014', 'POE-015', 'is held by'],
    ['POE-008', 'POE-014', 'feeds'],
    ['POE-011', 'POE-014', 'feeds'],
    ['POE-013', 'POE-015', 'frames'],
    ['POE-005', 'POE-015', 'is held by'],
    ['POE-010', 'POE-015', 'is held by'],
    ['POE-011', 'POE-015', 'is held by'],
  ],
};

export const REV_MAP: MapLayout = {
  nodes: {
    'REV-001': [70, 70, 1],
    'REV-002': [310, 70, 1],
    'REV-003': [550, 70, 1],
    'REV-004': [70, 220, 2],
    'REV-005': [250, 220, 2],
    'REV-006': [430, 220, 2],
    'REV-007': [610, 220, 2],
    'REV-008': [240, 370, 3],
    'REV-009': [480, 370, 3],
  },
  edges: [
    ['REV-001', 'REV-004', 'defines'],
    ['REV-002', 'REV-005', 'feeds'],
    ['REV-002', 'REV-006', 'feeds'],
    ['REV-003', 'REV-006', 'enables'],
    ['REV-004', 'REV-007', 'is met by'],
    ['REV-004', 'REV-008', 'is met by'],
    ['REV-005', 'REV-007', 'supports'],
    ['REV-006', 'REV-007', 'calls for'],
    ['REV-006', 'REV-009', 'demands'],
    ['REV-007', 'REV-009', 'requires'],
    ['REV-008', 'REV-009', 'frames'],
    ['REV-004', 'REV-009', 'raises'],
  ],
};

export const SCR_MAP: MapLayout = {
  nodes: {
    'SCR-001': [70, 70, 1],
    'SCR-002': [310, 70, 1],
    'SCR-003': [550, 70, 1],
    'SCR-004': [70, 220, 2],
    'SCR-005': [250, 220, 2],
    'SCR-006': [430, 220, 2],
    'SCR-007': [610, 220, 2],
    'SCR-008': [240, 370, 3],
    'SCR-009': [480, 370, 3],
  },
  edges: [
    ['SCR-001', 'SCR-005', 'feeds'],
    ['SCR-002', 'SCR-007', 'raises'],
    ['SCR-003', 'SCR-004', 'specifies'],
    ['SCR-003', 'SCR-009', 'is tested by'],
    ['SCR-005', 'SCR-006', 'reframes'],
    ['SCR-006', 'SCR-008', 'guides'],
    ['SCR-007', 'SCR-009', 'feeds'],
    ['SCR-004', 'SCR-009', 'is tested by'],
    ['SCR-001', 'SCR-008', 'grounds'],
    ['SCR-005', 'SCR-008', 'informs'],
  ],
};

export const AUT_MAP: MapLayout = {
  nodes: {
    'AUT-001': [70, 70, 1],
    'AUT-002': [310, 70, 1],
    'AUT-003': [550, 70, 1],
    'AUT-004': [70, 220, 2],
    'AUT-005': [250, 220, 2],
    'AUT-006': [430, 220, 2],
    'AUT-007': [610, 220, 2],
    'AUT-008': [240, 370, 3],
    'AUT-009': [480, 370, 3],
  },
  edges: [
    ['AUT-001', 'AUT-002', 'grounds'],
    ['AUT-001', 'AUT-003', 'grounds'],
    ['AUT-002', 'AUT-004', 'feeds'],
    ['AUT-003', 'AUT-004', 'feeds'],
    ['AUT-003', 'AUT-006', 'leads to'],
    ['AUT-004', 'AUT-005', 'is met by'],
    ['AUT-004', 'AUT-006', 'is met by'],
    ['AUT-005', 'AUT-009', 'frames'],
    ['AUT-006', 'AUT-007', 'leads to'],
    ['AUT-006', 'AUT-009', 'feeds'],
    ['AUT-007', 'AUT-008', 'informs'],
    ['AUT-008', 'AUT-009', 'raises'],
    ['AUT-004', 'AUT-009', 'is targeted by'],
  ],
};

export const CHR_MAP: MapLayout = {
  nodes: {
    'CHR-001': [70, 70, 1],
    'CHR-002': [310, 70, 1],
    'CHR-003': [550, 70, 1],
    'CHR-004': [70, 220, 2],
    'CHR-005': [250, 220, 2],
    'CHR-006': [430, 220, 2],
    'CHR-007': [610, 220, 2],
    'CHR-008': [240, 370, 3],
    'CHR-009': [480, 370, 3],
  },
  edges: [
    ['CHR-001', 'CHR-002', 'grounds'],
    ['CHR-001', 'CHR-003', 'grounds'],
    ['CHR-003', 'CHR-004', 'leads to'],
    ['CHR-002', 'CHR-007', 'feeds'],
    ['CHR-003', 'CHR-007', 'feeds'],
    ['CHR-004', 'CHR-007', 'raises'],
    ['CHR-004', 'CHR-008', 'is framed by'],
    ['CHR-005', 'CHR-008', 'is framed by'],
    ['CHR-005', 'CHR-006', 'extends'],
    ['CHR-001', 'CHR-006', 'grounds'],
    ['CHR-007', 'CHR-009', 'is targeted by'],
    ['CHR-008', 'CHR-009', 'frames'],
  ],
};

export const SAL_MAP: MapLayout = {
  nodes: {
    'SAL-001': [190, 70, 1],
    'SAL-002': [430, 70, 1],
    'SAL-003': [670, 70, 1],
    'SAL-004': [70, 220, 2],
    'SAL-005': [250, 220, 2],
    'SAL-006': [430, 220, 2],
    'SAL-007': [610, 220, 2],
    'SAL-008': [240, 370, 3],
    'SAL-009': [480, 370, 3],
  },
  edges: [
    ['SAL-001', 'SAL-002', 'leads to'],
    ['SAL-002', 'SAL-003', 'leads to'],
    ['SAL-003', 'SAL-004', 'raises'],
    ['SAL-003', 'SAL-006', 'ends in'],
    ['SAL-004', 'SAL-005', 'opens'],
    ['SAL-004', 'SAL-006', 'opens'],
    ['SAL-005', 'SAL-006', 'contrasts'],
    ['SAL-001', 'SAL-008', 'is tested by'],
    ['SAL-002', 'SAL-008', 'is tested by'],
    ['SAL-006', 'SAL-009', 'is targeted by'],
    ['SAL-007', 'SAL-009', 'frames'],
    ['SAL-003', 'SAL-007', 'is framed by'],
  ],
};

export const SYN_MAP: MapLayout = {
  nodes: {
    'SYN-001': [70, 70, 1],
    'SYN-002': [310, 70, 1],
    'SYN-003': [550, 70, 1],
    'SYN-004': [70, 220, 2],
    'SYN-005': [250, 220, 2],
    'SYN-006': [430, 220, 2],
    'SYN-007': [610, 220, 2],
    'SYN-008': [240, 370, 3],
    'SYN-009': [480, 370, 3],
  },
  edges: [
    ['SYN-001', 'SYN-002', 'leads to'],
    ['SYN-002', 'SYN-003', 'contrasts'],
    ['SYN-003', 'SYN-004', 'is framed by'],
    ['SYN-004', 'SYN-005', 'extends'],
    ['SYN-005', 'SYN-006', 'faces'],
    ['SYN-006', 'SYN-007', 'is tested by'],
    ['SYN-007', 'SYN-008', 'is met by'],
    ['SYN-008', 'SYN-009', 'is answered by'],
    ['SYN-004', 'SYN-008', 'is targeted by'],
    ['SYN-005', 'SYN-009', 'is held by'],
    ['SYN-002', 'SYN-009', 'is held by'],
    ['SYN-006', 'SYN-009', 'opens'],
  ],
};
