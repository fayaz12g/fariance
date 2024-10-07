package one.fayaz.fariance.blocks;

import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.block.FenceBlock;
import net.minecraft.world.level.block.state.BlockState;

public class CustomFenceBlock extends FenceBlock {
    public CustomFenceBlock(Properties properties) {
        super(properties);
    }

    @Override
    public boolean connectsTo(BlockState state, boolean isSideSolid, Direction direction) {
        return state.getBlock() instanceof FenceBlock || super.connectsTo(state, isSideSolid, direction);
    }
}