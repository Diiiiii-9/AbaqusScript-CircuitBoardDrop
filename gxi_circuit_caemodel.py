#
# Getting Started with ABAQUS
#
# Script for circuit board drop test example
#
from abaqus import *
import testUtils
testUtils.setBackwardCompatibility()
from abaqusConstants import *
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
session.journalOptions.setValues(replayGeometry=COORDINATE, 
    recoverGeometry=COORDINATE)
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()

session.viewports['Viewport: 1'].setValues(displayedObject=None)
mdb.models.changeKey(fromName='Model-1', toName='circuitBoard')

s = mdb.models['circuitBoard'].ConstrainedSketch(name='__profile__',
    sheetSize=0.1)
g, v, d = s.geometry, s.vertices, s.dimensions
s.sketchOptions.setValues(sheetSize=0.1, gridSpacing=0.002, grid=ON, 
    gridFrequency=2, constructionGeometry=ON, dimensionTextHeight=0.002, 
    decimalPlaces=3)
s.rectangle(point1=(-0.01, -0.012), point2=(0.01, 0.012))
p = mdb.models['circuitBoard'].Part(name='Packaging', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['circuitBoard'].parts['Packaging']
p.BaseSolidExtrude(sketch=s, depth=0.11)
s.unsetPrimaryObject()
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['circuitBoard'].sketches['__profile__']

p = mdb.models['circuitBoard'].parts['Packaging']
f, e = p.faces, p.edges
t = p.MakeSketchTransform(
    sketchPlane=f.findAt(coordinates=(-0.003333, -0.004, 0.11)),
    sketchUpEdge=e.findAt(coordinates=(0.01, 0.006, 0.11)), 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.11))
s = mdb.models['circuitBoard'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.228, gridSpacing=0.005, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(decimalPlaces=3)
s.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)

s.ConstructionLine(point1=(0.0, 0.012), angle=90.0)
s.VerticalConstraint(entity=g.findAt((0.0, 0.512)))
s.FixedConstraint(entity=g.findAt((0.0, 0.512)))

s.rectangle(point1=(-0.0030761412344873, 0.0162027012556791),
    point2=(0.0016987647395581, -0.00481949979439378))

s.SymmetryConstraint(entity1=g.findAt((-0.003076, 0.005692)),
    entity2=g.findAt((0.001699, 0.005692)),
    symmetryAxis=g.findAt((0.0, 0.512)))

s.HorizontalDimension(vertex1=v.findAt((-0.003076, -0.004819)), 
    vertex2=v.findAt((0.003076, -0.004819)),
    textPoint=(0.00270884111523628, -0.00729809980839491), value=0.002)

s.VerticalDimension(vertex1=v.findAt((0.01, 0.012)),
    vertex2=v.findAt((0.001, -0.004819)),
    textPoint=(0.0126259531825781, -0.00371789955534041), value=0.012)

p.CutExtrude(sketchPlane=f.findAt(coordinates=(-0.003333, -0.004, 0.11)), 
    sketchUpEdge=e.findAt(coordinates=(0.01, 0.006, 0.11)), 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, sketch=s, 
    flipExtrudeDirection=OFF)

s.unsetPrimaryObject()
del mdb.models['circuitBoard'].sketches['__profile__']

p.DatumPointByMidPoint(point1=p.InterestingPoint(edge=e.findAt(coordinates=(
    0.0005, 0.0, 0.11)), rule=MIDDLE), point2=p.InterestingPoint(
    edge=e.findAt(coordinates=(-0.0005, 0.0, 0.0)), rule=MIDDLE))

s = mdb.models['circuitBoard'].Sketch(name='__profile__', sheetSize=0.5)
g, v, d = s.geometry, s.vertices, s.dimensions
s.sketchOptions.setValues(sheetSize=0.5, gridSpacing=0.01, grid=ON, 
    gridFrequency=2, constructionGeometry=ON, dimensionTextHeight=0.01, 
    decimalPlaces=3)
s.rectangle(point1=(0.0, 0.0), point2=(0.1, 0.15))
session.viewports['Viewport: 1'].view.fitView()
p = mdb.models['circuitBoard'].Part(name='Board', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['circuitBoard'].parts['Board']
p.BaseShell(sketch=s)
p = mdb.models['circuitBoard'].parts['Board']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['circuitBoard'].sketches['__profile__']

p = mdb.models['circuitBoard'].parts['Board']
v = p.vertices
p.DatumPointByOffset(point=v.findAt(coordinates=(0.0, 0.0, 0.0)), vector=(
    0.01, 0.135, 0.0))
p.DatumPointByOffset(point=v.findAt(coordinates=(0.0, 0.0, 0.0)), vector=(
    0.07, 0.09, 0.0))
p.DatumPointByOffset(point=v.findAt(coordinates=(0.0, 0.0, 0.0)), vector=(
    0.08, 0.03, 0.0))

s = mdb.models['circuitBoard'].Sketch(name='__profile__', sheetSize=0.5)
g, v, d = s.geometry, s.vertices, s.dimensions
s.sketchOptions.setValues(sheetSize=0.5, gridSpacing=0.01, grid=ON, 
    gridFrequency=2, constructionGeometry=ON, dimensionTextHeight=0.01, 
    decimalPlaces=3)
s.rectangle(point1=(-0.1, -0.1), point2=(0.1, 0.1))
p = mdb.models['circuitBoard'].Part(name='Floor', dimensionality=THREE_D, 
    type=DISCRETE_RIGID_SURFACE)
p = mdb.models['circuitBoard'].parts['Floor']
p.BaseShell(sketch=s)
p = mdb.models['circuitBoard'].parts['Floor']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['circuitBoard'].sketches['__profile__']

p = mdb.models['circuitBoard'].parts['Floor']
p.ReferencePoint(point=(0.0, 0.0, 0.0))
session.viewports['Viewport: 1'].setValues(displayedObject=p)

mdb.models['circuitBoard'].Material('PCB')
mdb.models['circuitBoard'].materials['PCB'].Elastic(table=((45.e9, 0.3), ))
mdb.models['circuitBoard'].materials['PCB'].Density(table=((500.0, ), ))
mdb.models['circuitBoard'].Material('Foam')
mdb.models['circuitBoard'].materials['Foam'].Elastic(table=((3.e6, 0.0), ))
mdb.models['circuitBoard'].materials['Foam'].Density(table=((100.0, ), ))
mdb.models['circuitBoard'].materials['Foam'].CrushableFoam(table=((1.1, 0.1),))
mdb.models['circuitBoard'].materials['Foam'].crushableFoam.CrushableFoamHardening(table=(
    (220000.0, 0.0), (246510.0, 0.1), (272940.0, 0.2), (299020.0, 0.3), 
    (324550.0, 0.4), (349350.0, 0.5), (373260.0, 0.6), (396170.0, 0.7),
    (418010.0, 0.8), (438720.0, 0.9), (458270.0, 1.0), (493840.0, 1.2),
    (524840.0, 1.4), (551530.0, 1.6), (574310.0, 1.8), (593590.0, 2.0),
    (629360.0, 2.5), (651990.0, 3.0), (683340.0, 5.0), (688330.0, 10.0)))

mdb.models['circuitBoard'].HomogeneousShellSection(name='BoardSection', 
    preIntegrate=OFF, material='PCB', thickness=0.002, 
    poissonDefinition=DEFAULT, temperature=GRADIENT, integrationRule=SIMPSON, 
    numIntPts=5)

mdb.models['circuitBoard'].HomogeneousSolidSection(name='FoamSection', 
    material='Foam', thickness=1.0)

p = mdb.models['circuitBoard'].parts['Board']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f = p.faces
faces = f
region = regionToolset.Region(faces=faces)
p.SectionAssignment(region=region, sectionName='BoardSection')

p = mdb.models['circuitBoard'].parts['Packaging']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
c = p.cells
cells = c
region = regionToolset.Region(cells=cells)
p.SectionAssignment(region=region, sectionName='FoamSection')

p = mdb.models['circuitBoard'].parts['Board']
session.viewports['Viewport: 1'].setValues(displayedObject=p)

e = p.edges
p.DatumCsysByTwoLines(CARTESIAN,
    line1=e.findAt(coordinates=(0.025, 0.0, 0.0)),
    line2=e.findAt(coordinates=(0.1, 0.0375, 0.0)), name='Datum csys-1')

f = p.faces
faces = f
region = regionToolset.Region(faces=faces)
datums = p.datums[6]
p.assignMaterialOrientation(region=region, localCsys=datums, axis=AXIS_3)

a = mdb.models['circuitBoard'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)

a.DatumCsysByDefault(CARTESIAN)

p = mdb.models['circuitBoard'].parts['Floor']
a.Instance(name='Floor-1', part=p, dependent=ON)

a.DatumPointByCoordinate(coords=(0.0, 0.0, 0.0))
a.DatumPointByCoordinate(coords=(0.5, 0.707, 0.25))
r = a.instances['Floor-1'].referencePoints
d = a.datums
a.DatumAxisByTwoPoint(point1=r[2], point2=d[5])

p = mdb.models['circuitBoard'].parts['Packaging']
a.Instance(name='Packaging-1', part=p, dependent=ON)
mdb.models['circuitBoard'].rootAssembly.setValues(
   regenerateConstraintsTogether=OFF)

e = a.instances['Packaging-1'].edges
d = a.datums
a.EdgeToEdge(movableAxis=e.findAt(coordinates=(-0.01, -0.012, 0.0275)), 
    fixedAxis=d[6], flip=ON)

a.DatumPointByCoordinate(coords=(-0.5, 0.707, -0.5))
d = a.datums
a.DatumPlaneByLinePoint(line=d[6], point=d[10])

f = a.instances['Packaging-1'].faces
d = a.datums
a.FaceToFace(movablePlane=f.findAt(coordinates=(0.0179891354276455, 
    0.00658330416135736, 0.012563775694313)), fixedPlane=d[11], flip=ON, 
    clearance=0.0)

v = a.instances['Packaging-1'].vertices
r = a.instances['Floor-1'].referencePoints
a.CoincidentPoint(movablePoint=v.findAt(coordinates=(-0.0303476233973587, 
    -0.0429115394838653, -0.0151738116986794)), fixedPoint=r[2])

p = a.instances['Packaging-1']
p.ConvertConstraints()

p = a.instances['Floor-1']
p.translate(vector=(0.0, 0.0, -0.0001))

p = mdb.models['circuitBoard'].parts['Board']
a.Instance(name='Board-1', part=p, dependent=ON)

p = a.instances['Board-1']
p.translate(vector=(0.51, 0.0, 0.0))

f1 = a.instances['Board-1'].faces
f2 = a.instances['Packaging-1'].faces
a.ParallelFace(movablePlane=f1.findAt(coordinates=(0.543333333333333, 0.05, 
    0.0), normal=(0.0, 0.0, 1.0)), fixedPlane=f2.findAt(coordinates=(
    0.0272382919150449, 0.0177981609225068, 0.0273814785169062)), flip=OFF)

e1 = a.instances['Board-1'].edges
e2 = a.instances['Packaging-1'].edges
a.ParallelEdge(movableAxis=e1.findAt(coordinates=(0.596604525482204, 
    0.137963003192081, 0.0307533566177196)), fixedAxis=e2.findAt(coordinates=(
    0.0431590254312432, 0.0559914769973559, 0.0527683904196429)), flip=OFF)

e1 = a.instances['Board-1'].edges
d1 = a.instances['Packaging-1'].datums
a.CoincidentPoint(fixedPoint=d1[3],
    movablePoint=a.instances['Board-1'].InterestingPoint(
    edge=e1.findAt(coordinates=(0.652343827802905, 0.0916453486569404, 
    -0.0804357827095802)), rule=MIDDLE))

d = a.instances['Board-1'].datums
a.ReferencePoint(point=d[2])
a.ReferencePoint(point=d[3])
a.ReferencePoint(point=d[4])

r = a.referencePoints
refPoints1=(r[19], )
a.Set(referencePoints=refPoints1, name='TopChip')
refPoints1=(r[20], )
a.Set(referencePoints=refPoints1, name='MidChip')
refPoints1=(r[21], )
a.Set(referencePoints=refPoints1, name='BotChip')

e = a.instances['Board-1'].edges
edges = e.findAt(((0.0153385555521983, 0.0191710250695974, 
    0.0232637166281098), ))
a.Set(edges=edges, name='BotBoard')

region=a.sets['TopChip']
mdb.models['circuitBoard'].rootAssembly.engineeringFeatures.PointMassInertia(
    name='MassTopChip', region=region, mass=0.005, alpha=0.0, composite=0.0)

region=a.sets['MidChip']
mdb.models['circuitBoard'].rootAssembly.engineeringFeatures.PointMassInertia(
    name='MassMidChip', region=region, mass=0.005, alpha=0.0, composite=0.0)

region=a.sets['BotChip']
mdb.models['circuitBoard'].rootAssembly.engineeringFeatures.PointMassInertia(
    name='MassBotChip', region=region, mass=0.005, alpha=0.0, composite=0.0)

mdb.models['circuitBoard'].ExplicitDynamicsStep(name='Drop', 
    previous='Initial', timePeriod=0.02, massScaling=PREVIOUS_STEP)

regionDef=mdb.models['circuitBoard'].rootAssembly.sets['TopChip']
mdb.models['circuitBoard'].HistoryOutputRequest(name='H-Output-2', 
    createStepName='Drop', variables=('A3', 'V3'),
    timeInterval=0.0001, region=regionDef)

mdb.models['circuitBoard'].HistoryOutputRequest('H-Output-3', 
    mdb.models['circuitBoard'].historyOutputRequests['H-Output-2'])

regionDef=mdb.models['circuitBoard'].rootAssembly.sets['MidChip']
mdb.models['circuitBoard'].historyOutputRequests['H-Output-3'].setValues(
    region=regionDef)

mdb.models['circuitBoard'].HistoryOutputRequest('H-Output-4', 
    mdb.models['circuitBoard'].historyOutputRequests['H-Output-3'])

regionDef=mdb.models['circuitBoard'].rootAssembly.sets['BotChip']
mdb.models['circuitBoard'].historyOutputRequests['H-Output-4'].setValues(
    region=regionDef)

regionDef=mdb.models['circuitBoard'].rootAssembly.sets['BotBoard']
mdb.models['circuitBoard'].HistoryOutputRequest(name='H-Output-5', 
    createStepName='Drop', variables=('S11', 'S22', 'LEP'), 
    timeInterval=0.0001, region=regionDef, sectionPoints=(5, ))

mdb.models['circuitBoard'].ContactProperty('Fric')

mdb.models['circuitBoard'].interactionProperties['Fric'].TangentialBehavior(
    formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
    pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
    0.3, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
    fraction=0.005, elasticSlipStiffness=None)

mdb.models['circuitBoard'].ContactExp(name='All', createStepName='Drop')
mdb.models['circuitBoard'].interactions['All'].includedPairs.setValuesInStep(
    stepName='Drop', useAllstar=ON)
mdb.models['circuitBoard'].interactions['All'].contactPropertyAssignments.appendInStep(
    stepName='Drop', assignments=((GLOBAL, SELF, 'Fric'), ))

s = a.instances['Board-1'].faces
side12Faces = s
a.Surface(side12Faces=side12Faces, name='Board')

region1=a.surfaces['Board']
region2=a.sets['TopChip']
mdb.models['circuitBoard'].Tie(name='TopChip', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=OFF,  thickness=ON)

region1=a.surfaces['Board']
region2=a.sets['MidChip']
mdb.models['circuitBoard'].Tie(name='MidChip', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=OFF,  thickness=ON)

region1=a.surfaces['Board']
region2=a.sets['BotChip']
mdb.models['circuitBoard'].Tie(name='BotChip', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=OFF,  thickness=ON)

r = a.instances['Floor-1'].referencePoints
refPoints1=(r[2], )
a.Set(referencePoints=refPoints1, name='floorRefPt')

region = a.sets['floorRefPt']
mdb.models['circuitBoard'].EncastreBC(name='BC-1', createStepName='Initial', 
    region=region)

c = a.instances['Packaging-1'].cells
cells = c
f = a.instances['Packaging-1'].faces
faces1 = f
e = a.instances['Packaging-1'].edges
edges1 = e
v = a.instances['Packaging-1'].vertices
verts = v
f = a.instances['Board-1'].faces
faces2 = f
e = a.instances['Board-1'].edges
edges2 = e
r = a.referencePoints
refPoints=(r[19], r[20], r[21], )

region = regionToolset.Region(vertices=verts, edges=edges1+edges2, 
    faces=faces1+faces2, cells=cells, referencePoints=refPoints)
mdb.models['circuitBoard'].Velocity(name='Field-1', region=region, 
    velocity1=0.0, velocity2=0.0, velocity3=-4.43, omega=0.0)

p = mdb.models['circuitBoard'].parts['Board']
e = p.edges
pickedEdges = e.findAt(((0.025, 0.0, 0.0), ), ((0.1, 0.0375, 0.0), ), ((0.0, 
    0.1125, 0.0), ), ((0.075, 0.15, 0.0), ))
p.seedEdgeByNumber(edges=pickedEdges, number=10)

f = p.faces
faces = f
p.setMeshControls(regions=faces, technique=SWEEP)

elemType1 = mesh.ElemType(elemCode=S4R, elemLibrary=EXPLICIT, 
    secondOrderAccuracy=OFF, hourglassControl=RELAX_STIFFNESS)
elemType2 = mesh.ElemType(elemCode=S3R, elemLibrary=EXPLICIT)
regions =(faces, )
p.setElementType(regions=regions, elemTypes=(elemType1, elemType2))
p.generateMesh()
##
p = mdb.models['circuitBoard'].parts['Floor']
p.seedPart(size=1.0)

elemType1 = mesh.ElemType(elemCode=R3D4, elemLibrary=EXPLICIT)
elemType2 = mesh.ElemType(elemCode=R3D3, elemLibrary=EXPLICIT)
f = p.faces
faces = f
regions =(faces, )
p.setElementType(regions=regions, elemTypes=(elemType1, elemType2))
p.generateMesh()
##
p = mdb.models['circuitBoard'].parts['Packaging']
e = p.edges

edges =(e.findAt(coordinates=(0.0005, 0.0, 0.11)), )
p.seedEdgeByNumber(edges=edges, number=1)

edges = e.findAt(((0.001, 0.009, 0.11), ), ((-0.001, 0.003, 0.11), ), ((
    -0.00775, 0.012, 0.11), ), ((0.00325, 0.012, 0.11), ))
p.seedEdgeByNumber(edges=edges, number=3)

edges = e.findAt(((0.01, 0.006, 0.11), ))
p.seedEdgeByNumber(edges=edges, number=6)

edges = e.findAt(((0.005, -0.012, 0.11), ))
p.seedEdgeByNumber(edges=edges, number=7)

edges = e.findAt(((0.01, 0.012, 0.0275), ))
p.seedEdgeByNumber(edges=edges, number=15)

elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, 
    kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
    hourglassControl=ENHANCED)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=EXPLICIT)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)
c = p.cells
cells = c
regions =(cells, )
p.setElementType(regions=regions, elemTypes=(elemType1, elemType2, elemType3))
p.generateMesh()
##

session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Circuit', model='circuitBoard', type=ANALYSIS, 
    explicitPrecision=DOUBLE, description='Circuit board drop test')
session.viewports['Viewport: 1'].view.fitView()

a.regenerate()

session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    datumPoints=OFF, datumAxes=OFF, datumPlanes=OFF, datumCoordSystems=OFF)
session.viewports['Viewport: 1'].view.fitView()

mdb.saveAs('Circuit')

mdb.jobs['Circuit'].submit(consistencyChecking=OFF)

