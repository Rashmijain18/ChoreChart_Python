router.get("/getchildrenwithdetails", getChildrenWithDetails);
router.post("/createchild", createChild);
router.put("/updatechild", updateChild);
router.delete("/deletechild/:id", deleteChild);

router.get("/getallchores", getAllChores);
router.post("/createchore", createChore);
router.put("/updatechore/:id", updateChore);
router.delete("/deletechore/:id", deleteChore);
router.post("/assignchore", assignChore);
router.put("/updateChoreStatus/:choreId", updateChoreStatus);

// Dashboard routes
router.get("/childdashboard/:childId", getChildDashboard);
router.get("/parentdashboard/:parentId", getParentDashboard);

export default router;
